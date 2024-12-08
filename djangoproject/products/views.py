from django.shortcuts import render
from .models import ProductsVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def all_products(request):
    products = ProductsVariety.objects.all()
    return render(request, 'products/all_products.html', {'products':products})

def product_detail(request, product_id):
    product = get_object_or_404(ProductsVariety, pk = product_id)
    return render(request, 'products/product_detail.html', {'product':product})
