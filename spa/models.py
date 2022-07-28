from operator import mod
from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=25)

class Treatment(models.Model):
    treatment_name = models.CharField(max_length=25)
    treatment_category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, null=False, default='')
    treatment_rate = models.DecimalField(decimal_places=2)