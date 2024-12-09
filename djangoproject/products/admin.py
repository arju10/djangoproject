from django.contrib import admin
from .models import ProductsVariety, ProductReview, Store, ProductCertificate

# Register your models here.
class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    extra = 2

class ProductVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ProductReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal =('product_varieties',)

class ProductCertifateAdmin(admin.ModelAdmin):
    list_display = ('product', 'certificate_number')

admin.site.register(ProductsVariety, ProductVarityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ProductCertificate, ProductCertifateAdmin)