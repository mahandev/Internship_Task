from django.db import models

class Item(models.Model):
   name = models.CharField(max_length=2000)
   price = models.CharField(max_length=2000)
   location = models.CharField(max_length=2000)
   shop = models.CharField(max_length=2000)
   shop_rating = models.CharField(max_length=3)


   def __str__(self):
      return self.name
