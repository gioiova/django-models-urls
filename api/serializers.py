from rest_framework import serializers
from store.models import Category,Product


class CategoryListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('id','name')

class ProductSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(read_only=True)
    total = serializers.SerializerMethodField(method_name='total_price')
    
    def total_price(self, obj):
        return obj.price * obj.stock

    
    class Meta:
        model = Product
        fields = '__all__'
    

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        