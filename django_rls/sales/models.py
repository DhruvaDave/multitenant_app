from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Salesperson(User):
    class Meta:
        proxy = True
    
class Client(models.Model):
    name = models.CharField(max_length=50)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)