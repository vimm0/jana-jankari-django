from django.db import models
from django.utils.translation import ugettext_lazy as _


class Ministry(models.Model):
    name = models.CharField(_('name'), max_length=254)
    location = models.CharField(_('location'), max_length=254)

    class Meta:
        verbose_name = _('Ministry')
        verbose_name_plural = _('Ministries')

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(_('name'), max_length=254)
    location = models.CharField(_('location'), max_length=254)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

    def __str__(self):
        return self.name


# https://en.wikipedia.org/wiki/List_of_Nepal_government_organizations
class Office(models.Model):
    name = models.CharField(_('name'), max_length=254)
    website = models.URLField(_('website'), max_length=200)
    department = models.ForeignKey('Department', verbose_name=_('Department'), on_delete=models.CASCADE)
    ministry = models.ForeignKey('Ministry', verbose_name=_('Ministry'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Office')
        verbose_name_plural = _('Offices')

    def __str__(self):
        return self.name
