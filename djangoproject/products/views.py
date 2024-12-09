from django.shortcuts import render
from .models import ProductsVariety,  Store
from django.shortcuts import get_object_or_404
from .forms import ProductVarietyForm

# Create your views here.
def all_products(request):
    products = ProductsVariety.objects.all()
    return render(request, 'products/all_products.html', {'products':products})

def product_detail(request, product_id):
    product = get_object_or_404(ProductsVariety, pk = product_id)
    return render(request, 'products/product_detail.html', {'product':product})

def product_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ProductVarietyForm(request.POST)
        if form.is_valid():
            product_variety = form.cleaned_data['product_variety']
            stores = Store.objects.filter(product_varieties = product_variety)
    else:
        form = ProductVarietyForm()
    return render(request, 'products/product_stores.html',{'stores':stores, 'form':form} )
