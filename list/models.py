from django.db import models

# Create your models here.

class Product(models.Model):
    # atributos
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    bought= models.BooleanField()
    
    def __str__(self):
        return self.name