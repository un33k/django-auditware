from django.apps import apps
from django.apps import AppConfig as DjangoAppConfig
from django.utils.translation import ugettext_lazy as _


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
        from .receivers import latch_to_signals
        latch_to_signals()
