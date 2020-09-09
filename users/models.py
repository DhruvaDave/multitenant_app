from django.db import models

# Create your models here.
from tenant_schemas.models import TenantMixin


class User(models.Model):
    name = models.CharField(
        max_length=50, default='Ram Bahadur', null=True, blank=True)
    username = models.CharField(
        max_length=10, default='10minutes', null=True, blank=True)

    def __str__(self):
        return "Author - %s" % self.name


SHARED_APPS = (
    'tenant_schemas',  # mandatory, should always be before any django app
    'customers', # you must list the app where your tenant model resides in

    'django.contrib.contenttypes',
    
    # everything below here is optional
    # 'django.contrib.auth',
    # 'django.contrib.sessions',
    # # 'django.contrib.sites',
    # 'django.contrib.messages',
    # 'django.contrib.admin',
)

TENANT_APPS = (
    "users",
    "books",
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # your tenant-specific apps
    
    # 'myapp.hotels',
    # 'myapp.houses',
)

INSTALLED_APPS = [
    'tenant_schemas',

    'customers',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.sites',  
    'rest_framework', 

    "users",
    "books",
]