from rest_framework import serializers

from .models import *


class OwnCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnCheckModel
        fields = '__all__'
        read_only_fields = ['own_check_id']
