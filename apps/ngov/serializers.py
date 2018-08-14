from rest_framework import serializers

from apps.ngov.models import Ministry, Department, Office


class MinistrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ministry
        fields = ('name', 'location',)


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('name', 'location',)


class OfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Office
        fields = ('name', 'website', 'ministry', 'department')
