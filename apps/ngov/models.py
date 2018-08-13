from django.db import models


class Ministry(models.Model):
    name = models.CharField(max_length=254)
    location = models.CharField(max_length=254)


class Department(models.Model):
    name = models.CharField(max_length=254)
    location = models.CharField(max_length=254)


# https://en.wikipedia.org/wiki/List_of_Nepal_government_organizations
class Office(models.Model):
    name = models.CharField(max_length=254)
    website = models.URLField(max_length=200)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    ministry = models.ForeignKey('Ministry', on_delete=models.CASCADE)
