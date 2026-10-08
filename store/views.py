from django.shortcuts import render,HttpResponse,get_object_or_404
from django.http import JsonResponse
from store.models import Product,Category
from django.db.models import Count

# Create your views here.
def index(request):
    products = Product.objects.order_by('price')
    categories = Category.objects.annotate(product_count=Count('products')).filter(product_count__gt=0)
    return render(request, 'index.html', {'products': products, 'categories': categories})

def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category).order_by('price')
    return render(request, 'category.html', {'category': category, 'products': products})

def sale_products(request):
    sale_products = Product.objects.filter(is_sale=True)
    return render(request, 'sale_products.html', {'sale_products': sale_products})

def product_detail(request,product_id):
    product = get_object_or_404(Product,id = product_id)
    return render(request,'product_detail.html',{'product':product})