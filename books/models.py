from django.db import models

# Create your models here.
from tenant_schemas.models import TenantMixin


class Author(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "Author - %s" % self.name


class Book(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField(default=0.0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return "Book - %s" % str(self.pk)
