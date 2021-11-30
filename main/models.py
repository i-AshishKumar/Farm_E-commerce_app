from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    brand = models.CharField(max_length=50)
    Manufacturer = models.CharField(max_length=50,default=None)
    Country = models.CharField(max_length=50,default=None)
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-price']