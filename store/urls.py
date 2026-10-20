from django.urls import path
from store.views import IndexView,delete_product,SaleProductListView,ProductDetailView,ProductCreateView,CategoryView

app_name='store'

urlpatterns = [
    # path('', index, name='index'),
    path('', IndexView.as_view(), name='index'),
    # path('category/<int:category_id>/', category_view, name='category'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category'),
    # path('sale/', sale_products, name='sale_products'),
    path('sale/', SaleProductListView.as_view(), name='sale_products'),
    # path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    # path('add_product/', add_product, name='add_product'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('delete_product/<int:product_id>/',delete_product,name='delete_product'),
]