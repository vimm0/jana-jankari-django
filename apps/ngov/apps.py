from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class NgovConfig(AppConfig):
    name = 'apps.ngov'
    verbose_name = _('ngov')
