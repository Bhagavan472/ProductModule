from django.db import models

# Create your models here.
class product(models.Model):
    location=models.CharField(max_length=100)
    farm=models.CharField(max_length=100)
    product=models.CharField(max_length=100)
    quantity=models.DecimalField(max_digits=10, decimal_places=2)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    
