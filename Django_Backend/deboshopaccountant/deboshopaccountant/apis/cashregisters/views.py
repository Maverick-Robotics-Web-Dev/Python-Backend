from rest_framework import viewsets, permissions

from .models import *
from .serializers import *


class CashRegisterViewSet(viewsets.ModelViewSet):
    queryset = CashRegisterModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CashRegisterSerializer


class CashRegisterOpeningViewSet(viewsets.ModelViewSet):
    queryset = CashRegisterOpeningModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CashRegisterOpeningSerializer


class CashRegisterMovementsViewSet(viewsets.ModelViewSet):
    queryset = CashRegisterMovementsModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CashRegisterMovementsSerializer


class CashRegisterClosingViewSet(viewsets.ModelViewSet):
    queryset = CashRegisterClosingModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CashRegisterClosingSerializer
