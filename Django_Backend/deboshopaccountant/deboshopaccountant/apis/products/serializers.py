from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'
        read_only_fields = ['category_id']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = '__all__'
        read_only_fields = ['brand_id']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
        read_only_fields = ['product_id']
