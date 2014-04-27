from django.shortcuts import render
from products.models import Product

# Create your views here.
def list_products(request):
    products = Product.objects.order_by('title')
    context = {'products': products}
    return render(request, 'product_list.html', context)
    

