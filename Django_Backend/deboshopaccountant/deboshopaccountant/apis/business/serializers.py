from rest_framework import serializers

from .models import *


class WayToPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WayToPayModel
        fields = '__all__'
        read_only_fields = ['way_to_pay_id']


class VoucherTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoucherTypeModel
        fields = '__all__'
        read_only_fields = ['voucher_type_id']


class CreditNoteSerializaer(serializers.ModelSerializer):
    class Meta:
        model = CreditNoteModel
        fields = '__all__'
        read_only_fields = ['credit_note_id']


class CreditNoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditNoteDetailModel
        fields = '__all__'
        read_only_fields = ['credit_note_detail_id']


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleModel
        fields = '__all__'
        read_only_fields = ['sale_id']


class SaleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetailModel
        fields = '__all__'
        read_only_fields = ['sale_detail_id']
