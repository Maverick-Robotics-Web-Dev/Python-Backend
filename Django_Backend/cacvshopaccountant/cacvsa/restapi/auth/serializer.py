from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import *


class CustomJwtTokenSerializer(TokenObtainPairSerializer):
    pass


class UserLoginSerializer(ModelSerializer):

    class Meta:
        model = UserEmployeeModel
        fields = ['id', 'user_employee_user_name']
        read_only_fields = ['id', 'user_employee_user_name']
