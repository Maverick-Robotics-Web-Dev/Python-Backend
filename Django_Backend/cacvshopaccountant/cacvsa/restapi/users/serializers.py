from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import *


class UserLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLevelModel
        fields = '__all__'
        read_only_fields = ['user_level_id']


class UserEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEmployeeModel
        fields = '__all__'
        read_only_fields = ['user_employee_id']


class UserClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClientModel
        fields = '__all__'
        read_only_fields = ['user_client_id']


class CustomJwtToken(TokenObtainPairSerializer):
    pass
