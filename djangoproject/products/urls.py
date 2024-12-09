from django.urls import path
from . import views

# localshost:8000/products
# localshost:8000/products/order

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('product_stores/', views.product_store_view, name='product_stores')

]
