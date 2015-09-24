import logging
from django.contrib.auth import signals as django_signals
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from ipware.ip import get_ip

from .models import UserAudit
from . import utils as util
from . import defaults as defs

log = logging.getLogger('auditware.listeners')


def user_audit_create(sender, user, request, **kwargs):
    """ Create a user activity audit when user is logged in """

    audit_key = util.get_audit_key(request.session.session_key)
    try:
        uaa = UserAudit.objects.get(audit_key=audit_key)
    except UserAudit.DoesNotExist:
        data = {
            'user': request.user,
            'audit_key': audit_key,
            'user_agent': request.META.get('HTTP_USER_AGENT', 'Unknown'),
            'ip_address': get_ip(request),
            'referrer': request.META.get('HTTP_REFERER', 'Unknown'),
            'last_page': request.path or '/',
        }
        uaa = UserAudit(**data)
    log.info(_('User {0} logged in'.format(request.user.username)))
    uaa.save()
    request.session[defs.ACTIVITYWARE_AUDIT_KEY] = audit_key
    request.session.modified = True
    util.cleanup_user_audits(request.user)


def user_audit_delete(sender, user, request, **kwargs):
    """ Delete a user activity audit when user is logged out """

    try:
        UserAudit.objects.get(audit_key=request.session[defs.ACTIVITYWARE_AUDIT_KEY]).delete()
    except:
        pass
    log.info(_('User {0} logged out'.format(request.user.username)))


def latch_to_signals():
    """
    Latch to the signals we are interested in.
    """
    User = get_user_model()

    # Latch on to login signal
    django_signals.user_logged_in.connect(user_audit_create, sender=User,
                                     dispatch_uid='user_audit_create_call_me_only_once_please')

    # Latch on logout signal
    django_signals.user_logged_out.connect(user_audit_delete, sender=User,
                                       dispatch_uid='user_audit_delete_call_me_only_once_please')
