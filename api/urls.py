from django.urls import path, include
from .views import CategoryListAPIView, ProductListAPIView,ProductRetrieveAPIView,ProductCreateAPIView
app_name = 'api'

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('products/', ProductListAPIView.as_view(), name='product_list'),
    path('products/<int:product_pk>/', ProductRetrieveAPIView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product_create'),
]