from django.urls import path
from . import views

# localshost:8000/products
# localshost:8000/products/order

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('order/', views.order, name= 'order'),
]
