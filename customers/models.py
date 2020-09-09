from django.db import models

# Create your models here.
from tenant_schemas.models import TenantMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until =  models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)
    # test = models.CharField(null=True,blank=True,max_length=100)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True