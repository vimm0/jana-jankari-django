import datetime
from haystack import indexes

from apps.ngov.models import Office, Department


# class OfficeIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     name = indexes.CharField(model_attr='name')
#     website = indexes.CharField(model_attr='website')
#     # department = indexes.CharField(model_attr='department__id')
#     # ministry = indexes.CharField(model_attr='ministry__id')
#     department_name = indexes.CharField(model_attr='department__id')
#     ministry_name = indexes.CharField(model_attr='ministry__id')
#
#     def prepare_department_name(self, obj):
#         # import ipdb
#         # ipdb.set_trace()
#         return '' if not obj.department else obj.department.name
#
#     def prepare_ministry_name(self, obj):
#         return '' if not obj.ministry else obj.ministry.name
#
#     def get_model(self):
#         return Office
#
#     def index_queryset(self, using=None):
#         """Used when the entire index for model is updated."""
#         # return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
#         # import ipdb
#         # ipdb.set_trace()
#         return self.get_model().objects.all().select_related('department', 'ministry')


class DepartmentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    location = indexes.CharField(model_attr='location')


    def get_model(self):
        return Department

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        # return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
        return self.get_model()