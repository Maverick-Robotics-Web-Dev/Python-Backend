from typing import Any, Self
from rest_framework.serializers import (
    ModelSerializer, Serializer, CharField, ValidationError)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from restapi.users.models import *


class CustomJwtTokenSerializer(TokenObtainPairSerializer):
    pass


class LoginSerializer(ModelSerializer):

    class Meta:

        model: UserEmployeeModel = None
        fields: list[str] = None
        read_only_fields: list[str] = None

        model = UserEmployeeModel
        fields = ['id', 'user_employee_user_name', 'user_employee_login']
        read_only_fields = ['id']


class PasswordChangeSerializer(Serializer):

    password: CharField = None
    confirm_password: CharField = None

    password = CharField(max_length=128, write_only=True)
    confirm_password = CharField(max_length=128, write_only=True)

    def validate(self: Self, data: Any) -> Any:
        if data['password'] != data['confirm_password']:
            raise ValidationError(
                {'password': 'No coinciden las contraseñas'})
        return data
