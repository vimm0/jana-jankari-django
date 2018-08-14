from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from apps.ngov.models import Ministry, Department, Office


class MinistryAdmin(TranslationAdmin):
    list_display = ('name', 'location',)


class DepartmentAdmin(TranslationAdmin):
    list_display = ('name', 'location',)


class OfficeAdmin(TranslationAdmin):
    list_display = ('name', 'website', 'ministry', 'department',)


admin.site.register(Ministry, MinistryAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Office, OfficeAdmin)
# TODO: Add localization in Admin success message, recent action logs
