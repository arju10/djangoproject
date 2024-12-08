from django.shortcuts import render
from .models import ProductsVariety

# Create your views here.
def all_products(request):
    products = ProductsVariety.objects.all()
    return render(request, 'products/all_products.html', {'products':products})

def order(request):
    return render(request, 'products/all_products.html')