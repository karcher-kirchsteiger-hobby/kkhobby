from django.contrib import admin
from products.models import Product
from products.models import Tag
from products.models import ProductImage
from products.models import ProductFamily
# Register your models here.
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(ProductImage)
admin.site.register(ProductFamily)
