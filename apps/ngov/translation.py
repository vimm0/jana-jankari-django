from modeltranslation.translator import TranslationOptions, translator

from apps.ngov.models import Ministry, Department, Office


class MinistryTranslationOptions(TranslationOptions):
    fields = ('name', 'location',)


class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'location',)


class OfficeTranslationOptions(TranslationOptions):
    fields = ('name', 'website', 'ministry', 'department',)


translator.register(Ministry, MinistryTranslationOptions)
translator.register(Department, DepartmentTranslationOptions)
translator.register(Office, OfficeTranslationOptions)
