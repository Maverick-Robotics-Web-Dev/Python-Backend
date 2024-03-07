from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from restapi.users.models import *
# from restapi.support.methods import get_token_model


class CustomJwtTokenSerializer(TokenObtainPairSerializer):
    pass


class LoginSerializer(ModelSerializer):

    class Meta:
        model = UserEmployeeModel
        fields = ['id', 'user_employee_user_name', 'user_employee_login']
        read_only_fields = ['id']


class PasswordChangeSerializer(Serializer):

    password = serializers.CharField(max_length=128, write_only=True)
    confirm_password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(
                {'password': 'No coinciden las contraseñas'})
        return data
