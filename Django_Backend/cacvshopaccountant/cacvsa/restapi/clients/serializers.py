from rest_framework import serializers

from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = '__all__'
        read_only_fields = ['client_id']


class ClientCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientCheckModel
        fields = '__all__'
        read_only_fields = ['client_check_id']
