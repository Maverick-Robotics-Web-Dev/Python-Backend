from rest_framework import serializers

from .models import *


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierModel
        fields = '__all__'
        read_only_fileds = ['supplier_id']


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeModel
        fields = '__all__'
        read_only_fileds = ['income_id']


class IncomeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeDetailModel
        fields = '__all__'
        read_only_fileds = ['income_detail_id']
