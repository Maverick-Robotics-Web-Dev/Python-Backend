from rest_framework import serializers

from .models import *


class CashRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashRegisterModel
        fields = '__all__'
        read_only_fields = ['cash_register_id']


class CashRegisterOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashRegisterOpeningModel
        fields = '__all__'
        read_only_fields = ['cash_register_opening_id']


class CashRegisterMovementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashRegisterMovementsModel
        fields = '__all__'
        read_only_fields = ['cash_register_movements_id']


class CashRegisterClosingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashRegisterClosingModel
        fields = '__all__'
        read_only_fields = ['cash_register_closing_id']
