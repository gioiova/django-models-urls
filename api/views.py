from rest_framework.decorators import api_view,permission_classes
from store.models import Category, Product, Category
from rest_framework.response import Response
from .serializers import CategoryListSerializer,ProductSerializer,ProductListSerializer,ProductCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView

# @api_view(['GET'])
# def product_list(request):
#     products = Product.objects.values()
#     return Response(products)

# @api_view(['GET'])
# def category_list(request):
#     categories = Category.objects.all()
#     serializer = CategoryListSerializer(categories, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductListSerializer(products, many=True)
#     return Response(serializer.data)


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_pk'

class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated]
    
