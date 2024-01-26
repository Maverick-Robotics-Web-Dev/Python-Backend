from rest_framework import viewsets, permissions

from .models import *
from .serializers import *


class ClientViewSet(viewsets.ModelViewSet):
    queryset = ClientModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientSerializer


class ClientCheckViewSet(viewsets.ModelViewSet):
    queryset = ClientCheckModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientCheckSerializer
