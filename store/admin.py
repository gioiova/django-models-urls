from django.contrib import admin
from .models import Product, Category

# Register your models here.

# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','is_sale')
    #list_display_links =('name','price','stock')
    list_editable = ('price','stock','is_sale')
    search_fields = ('name','description')