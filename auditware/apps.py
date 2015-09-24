from django.apps import apps
from django.apps import AppConfig as DjangoAppConfig
from django.utils.translation import ugettext_lazy as _

from .receivers import latch_to_signals


class AppConfig(DjangoAppConfig):
    """
    Configuration entry point for the auditware app
    """
    label = name = 'auditware'
    verbose_name = _("auditware app")

    def ready(self):
        """
        App is imported and ready, so bootstrap it.
        """
        latch_to_signals()
