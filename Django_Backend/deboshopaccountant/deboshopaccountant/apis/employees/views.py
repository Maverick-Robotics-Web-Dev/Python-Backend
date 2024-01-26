from rest_framework import viewsets, permissions

from .models import *
from .serializers import *


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmployeeSerializer
