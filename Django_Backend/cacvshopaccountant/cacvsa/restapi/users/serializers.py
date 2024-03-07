from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import *


class UserLevelSerializer(ModelSerializer):
    class Meta:
        model = UserLevelModel
        fields = '__all__'
        read_only_fields = ['user_level_id']


class UserEmployeeSerializer(ModelSerializer):
    class Meta:
        model = UserEmployeeModel
        # fields = '__all__'
        exclude = ['groups', 'user_permissions']
        read_only_fields = ['user_employee_id']


class UserClientSerializer(ModelSerializer):
    class Meta:
        model = UserClientModel
        fields = '__all__'
        read_only_fields = ['user_client_id']
