from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from apps.ngov.models import Ministry, Department, Office


class MinistryAdmin(TranslationAdmin):
    list_display = ('name', 'location',)


class DepartmentAdmin(TranslationAdmin):
    list_display = ('name', 'location',)


class OfficeAdmin(TranslationAdmin):
    list_display = ('name', 'website', 'department', 'ministry')

    list_select_related = (
        'department',
        'ministry',
    )
    raw_id_fields = ('ministry', 'department',)

    # def get_queryset(self, request):
    #     return super(OfficeAdmin, self).get_queryset(request).select_related('ministry', 'department')
    # pass


admin.site.register(Ministry, MinistryAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Office, OfficeAdmin)
# TODO: Add localization in Admin success message, recent action logs
# TODO:  Optimize each model for Duplicated 2 times.
