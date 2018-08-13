from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.ngov.api import MinistryViewSet, DepartmentViewSet, OfficeViewSet

router = routers.DefaultRouter()
router.register('ministry', MinistryViewSet)
router.register('department', DepartmentViewSet)
router.register('office', OfficeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # path(r'^api-auth/', include('rest_framework.urls'))

]
