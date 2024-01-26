from rest_framework import viewsets, permissions

from .models import *
from .serializers import *


class UserLevelViewSet(viewsets.ModelViewSet):
    queryset = UserLevelModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLevelSerializer


class UserEmployeeViewSet(viewsets.ModelViewSet):
    queryset = UserEmployeeModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserEmployeeSerializer


class UserClientViewSet(viewsets.ModelViewSet):
    queryset = UserClientModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserClientSerializer
