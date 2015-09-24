from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import logout
from django.contrib import messages

from ..models import UserAudit
from .. import defaults as defs


class LogoutEnforcementMiddleware(object):
    """
    Logout enforcement Middleware.
    """
    def process_request(self, request):
        """
        Logout user if required.
        """
        if request.user.is_authenticated():
            try:
                uaa = UserAudit.objects.get(audit_key=request.session[defs.AUDITWARE_SESSION_KEY])
            except:  # catch all
                logout(request)  # we shouldn't be here
            else:
                if uaa and uaa.force_logout:
                    messages.add_message(request, messages.WARNING,
                        _('Warning!. This session was terminated remotely by the owner of the account.'))
                    logout(request)
        return None
