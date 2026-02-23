from symtable import Class

from django.db import models

# Create your models here.

class Cart(models.Model):
    productname = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.productname
