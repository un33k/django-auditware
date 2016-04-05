from django.conf import settings
from django.db import models

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class UserAudit(models.Model):
    """
    User Audit Model.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(AUTH_USER_MODEL, related_name="%(class)s")
    audit_key = models.CharField(max_length=255, db_index=True, unique=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    referrer = models.CharField(max_length=255)
    user_agent = models.CharField(max_length=255)
    last_page = models.CharField(max_length=255)
    pages_viwed = models.PositiveIntegerField(default=0)
    force_logout = models.BooleanField(default=False)

    class Meta:
        unique_together = (("user", "audit_key"),)

    def __unicode__(self):
        return u"{} ({})".format(self.user.email, self.ip_address)
