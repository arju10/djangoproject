from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    

# One to many
class ProductReview(models.Model):
    product = models.ForeignKey(ProductsVariety, on_delete= models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username}  review for {self.product.name}'
    
# Many to Many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    product_varieties = models.ManyToManyField(ProductsVariety, related_name='store')

    def __str__(self):
        return self.name
    
# One to One
class ProductCertificate(models.Model):
    product = models.OneToOneField(ProductsVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_till = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.product}'