from django.urls import path
from store.views import index,category_view,sale_products,product_detail,add_product,delete_product

app_name='store'

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', category_view, name='category'),
    path('sale/', sale_products, name='sale_products'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('add_product/', add_product, name='add_product'),
    path('delete_product/<int:product_id>/',delete_product,name='delete_product'),
]