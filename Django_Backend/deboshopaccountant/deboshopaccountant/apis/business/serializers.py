from rest_framework import serializers

from .models import WayToPayModel

class WayToPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WayToPayModel
        fields = '__all__'
        read_only_fields =['way_to_pay_create_at', 'way_to_pay_update_at']