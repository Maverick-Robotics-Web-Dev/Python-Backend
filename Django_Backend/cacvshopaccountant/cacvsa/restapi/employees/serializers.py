from rest_framework.serializers import (
    ModelSerializer,
    StringRelatedField
)

from .models import EmployeeModel


class EmployeeSerializer(ModelSerializer):

    class Meta:

        model: EmployeeModel = None
        fields: str = None

        model = EmployeeModel
        fields = '__all__'


class EmployeeRelatedSerializer(ModelSerializer):

    fk_user_employee: StringRelatedField = None

    fk_user_employee = StringRelatedField()

    class Meta:

        model: EmployeeModel = None
        fields: str = None

        model = EmployeeModel
        fields = '__all__'
