from typing import Self
from collections import OrderedDict
from datetime import datetime

from rest_framework.serializers import (
    ModelSerializer,
    StringRelatedField
)

from .models import (
    CategoryModel,
    BrandModel,
    ProductModel
)


class CategorySerializer(ModelSerializer):

    class Meta:

        model: CategoryModel = None
        # fields: str = None
        # exclude: list = None

        model = CategoryModel
        fields = '__all__'
        # exclude = ['create_at']

    def create(self: Self, validated_data: OrderedDict):
        validated_data["status"] = True
        print(validated_data['create_at'])
        print(type(validated_data))
        print(validated_data)

        return self.Meta.model._default_manager.create(**validated_data)


class CategoryRelatedSerializer(ModelSerializer):

    fk_user_employee: StringRelatedField = None

    fk_user_employee = StringRelatedField()

    class Meta:

        model: CategoryModel = None
        fields: str = None

        model = CategoryModel
        fields = '__all__'


class BrandSerializer(ModelSerializer):

    class Meta:

        model: BrandModel = None
        fields: str = None

        model = BrandModel
        fields = '__all__'


class BrandRelatedSerializer(ModelSerializer):

    fk_user_employee: StringRelatedField = None

    fk_user_employee = StringRelatedField()

    class Meta:

        model: BrandModel = None
        fields: str = None

        model = BrandModel
        fields = '__all__'


class ProductSerializer(ModelSerializer):

    class Meta:

        model: ProductModel = None
        fields: str = None

        model = ProductModel
        fields = '__all__'


class ProductRelatedSerializer(ModelSerializer):

    fk_supplier: StringRelatedField = None
    fk_category: StringRelatedField = None
    fk_brand: StringRelatedField = None
    fk_user_employee: StringRelatedField = None

    fk_supplier = StringRelatedField()
    fk_category = StringRelatedField()
    fk_brand = StringRelatedField()
    fk_user_employee = StringRelatedField()

    class Meta:

        model: ProductModel = None
        fields: str = None

        model = ProductModel
        fields = '__all__'
