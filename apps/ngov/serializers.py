from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

from apps.ngov.models import Ministry, Department, Office


class MinistrySerializer(serializers.HyperlinkedModelSerializer):
    name_ = serializers.ReadOnlyField(source='get_name')
    location_ = serializers.ReadOnlyField(source='get_location')

    class Meta:
        model = Ministry
        fields = ('name_', 'location_')

    def get_name(self):
        return _(self.name)

    def get_location(self):
        return _(self.location)


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class OfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'
