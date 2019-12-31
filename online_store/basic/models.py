from django.db import models

# Create your models here.
class Combined_item(models.Model):
    collection_name  =  models.CharField(max_length=30)
    original_price   =  models.IntegerField()
    discounted_price =  models.IntegerField()
    items            =  models.CharField(max_length=100)

