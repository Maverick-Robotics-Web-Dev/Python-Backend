from rest_framework import viewsets, permissions

from .models import *
from .serializers import *


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = SupplierModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SupplierSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = IncomeModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = IncomeSerializer


class IncomeDetailViewSet(viewsets.ModelViewSet):
    queryset = IncomeDetailModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = IncomeDetailSerializer
