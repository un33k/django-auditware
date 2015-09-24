from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import logout
from django.contrib import messages

from ..models import UserAudit
from .. import defaults as defs


class UserAuditMiddleware(object):

    def process_request(self, request):
        """
        Monitor User's Activity.
        """
        if not request.is_ajax() and request.user.is_authenticated():
            try:
                uaa = UserAudit.objects.get(audit_key=request.session[defs.ACTIVITYWARE_AUDIT_KEY])
            except:
                logout(request)  # we shouldn't be here
            else:
                if uaa and uaa.last_page != request.path:
                    uaa.last_page = request.path
                    uaa.pages_viwed += 1
                    uaa.save()
        return None
