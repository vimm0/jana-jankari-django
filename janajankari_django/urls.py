from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from rest_framework import routers

from apps.ngov.api import MinistryViewSet, DepartmentViewSet, OfficeViewSet

router = routers.DefaultRouter()
router.register('ministry', MinistryViewSet)
router.register('department', DepartmentViewSet)
router.register('office', OfficeViewSet)

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # path(r'^api-auth/', include('rest_framework.urls'))
)
