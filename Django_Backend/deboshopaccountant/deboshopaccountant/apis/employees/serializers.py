from rest_framework import serializers

from .models import *


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__'
        read_only_fields = ['employee_id']
