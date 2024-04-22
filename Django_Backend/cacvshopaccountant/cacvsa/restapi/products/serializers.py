from typing import Self
from collections import OrderedDict
from datetime import datetime
import pytz

from django.db.models import (DecimalField)

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
        fields: str = None
        # exclude: list = None

        model = CategoryModel
        fields = '__all__'
        # exclude = ['create_at']

    def create(self: Self, validated_data: OrderedDict):
        validated_data["status"] = True
        srlz = validated_data['create_at']

        tr: DecimalField = DecimalField(max_digits=11, decimal_places=2)
        tr2: DecimalField = DecimalField(max_digits=11, decimal_places=2)
        total: DecimalField = DecimalField(max_digits=11, decimal_places=2)
        iva: DecimalField = DecimalField(max_digits=11, decimal_places=2)
        totaliva: DecimalField = DecimalField(max_digits=11, decimal_places=2)

        tr = 4.02
        tr2 = 3.39
        total = tr+tr2
        print(f'########## TERMINOS ##########')
        print(f'Termino 1: {tr}')
        print(f'Termino 2: {tr2}')
        print(f'########## TOTAL ##########')
        print(f'Total: {total}')
        iva = tr*0.12
        totaliva = tr+iva
        print(f'########## TOTAL IVA ##########')
        print(f'IVA: {iva}')
        print(f'Total iva: {totaliva}')

        dt = datetime.now()
        dtc = dt.strftime('%Y-%m-%d %H:%M:%S.%f+00:00')
        dtsp = datetime.strptime(dtc, '%Y-%m-%d %H:%M:%S.%f%z')
        dtu = pytz.timezone('UTC').localize(dt)
        madrid = pytz.timezone('Europe/Madrid').localize(dt)
        validated_data['create_at'] = dtu
        print(f'########## SERIALIZER ##########')
        print(f'{srlz.tzinfo}: {srlz}')
        print(f'########## PYTZ ##########')
        print(f'{dtu.tzinfo}: {dtu}')
        print(f'{madrid.tzinfo}: {madrid}')
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
