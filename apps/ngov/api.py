from rest_framework import viewsets

from apps.ngov.models import Ministry, Department, Office
from apps.ngov.serializers import MinistrySerializer, DepartmentSerializer, OfficeSerializer


class MinistryViewSet(viewsets.ModelViewSet):
    queryset = Ministry.objects.all()
    serializer_class = MinistrySerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
