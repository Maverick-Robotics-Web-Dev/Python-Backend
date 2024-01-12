from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import *
from .serializers import *


class WayToPayViewSet(viewsets.ModelViewSet):
    queryset = WayToPayModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = WayToPaySerializer


class VoucherTypeViewSet(viewsets.ModelViewSet):
    queryset = VoucherTypeModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = WayToPaySerializer
