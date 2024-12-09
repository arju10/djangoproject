from django import forms
from .models import ProductsVariety

class ProductVarietyForm(forms.Form):
    product_variety = forms.ModelChoiceField(queryset=ProductsVariety.objects.all(), label="Select Product Variety")

    