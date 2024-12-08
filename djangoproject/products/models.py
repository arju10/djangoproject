from django.db import models
from django.utils import timezone

class ProductsVariety(models.Model):
    PRODUCT_TYPE_CHOICE = [
        ('MOUSE', 'Mouse'),
        ('KEYBOARD', 'Keyboard'),
        ('RAM', 'RAM'),
        ('HARD-DISK', 'Hard Disk'),
        ('WINDOWS 11', 'Windows 11'),
        ('WINDOWS 10', 'Windows 10'),
        ('LAPTOP', 'Laptop'),
        ('DESKTOP', 'Desktop'),
        ('MOBILE CHARGER', 'Mobile Charger'),
        ('LAPTOP CHARGER', 'Laptop Charger'),
    ]

    name = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='products/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICE)  
    description = models.TextField(default='')

    def __str__(self):
        return self.name