from django.contrib import admin

from apps.ngov.models import Ministry, Department, Office

admin.site.register(Ministry)
admin.site.register(Department)
admin.site.register(Office)
