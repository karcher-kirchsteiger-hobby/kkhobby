from django.db import models
from decimal import Decimal
    
class ProductFamily (models.Model):
    title = models.CharField(max_length=200)
    def __unicode__(self):
        return self.title
    
class Tag (models.Model):
    title = models.CharField(max_length=200)    
    def __unicode__(self):
        return self.title

class Product (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    family = models.ForeignKey(ProductFamily)
    quantity = models.IntegerField()
    def __unicode__(self):
        return self.title
       
class ProductImage (models.Model):
    image = models.ImageField(upload_to='product_images')
    description = models.TextField()
    headline = models.CharField(max_length=200)
    product = models.ForeignKey(Product)
    def __unicode__(self):
        return self.headline
