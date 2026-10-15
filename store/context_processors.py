from django.db.models import Count
from store.models import Product, Category


def products(request):
    return {
        'My_site': 'store',
        'product_list': Product.objects.all(),
        'categories': Category.objects.annotate(product_count=Count('products')).filter(product_count__gt=0),
    }
