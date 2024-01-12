from rest_framework import serializers

from .models import *


class WayToPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WayToPayModel
        fields = '__all__'
        read_only_fields = ['way_to_pay_id',
                            'way_to_pay_create_at', 'way_to_pay_update_at']


class VoucherTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoucherTypeModel
        fields = '__all__'
        read_only_fields = ['voucher_type_id',
                            'voucher_type_create_at', 'voucher_type_update_at']
