from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import *
from .serializers import *


class WayToPayViewSet(viewsets.ModelViewSet):
    queryset = WayToPayModel.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = WayToPaySerializer


class VoucherTypeViewSet(viewsets.ModelViewSet):
    queryset = VoucherTypeModel.objects.all()
    # permission_classes = [AllowAny]
    serializer_class = VoucherTypeSerializer


class CreditNoteViewSet(viewsets.ModelViewSet):
    queryset = VoucherTypeModel.objects.all()
    # permission_classes = [AllowAny]
    serializer_class = CreditNoteSerializaer


class CreditNoteDetailViewSet(viewsets.ModelViewSet):
    queryset = VoucherTypeModel.objects.all()
    # permission_classes = [AllowAny]
    serializer_class = CreditNoteDetailSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = VoucherTypeModel.objects.all()
    # permission_classes = [AllowAny]
    serializer_class = SaleSerializer


class SaleDetailViewSet(viewsets.ModelViewSet):
    queryset = VoucherTypeModel.objects.all()
    # permission_classes = [AllowAny]
    serializer_class = SaleDetailSerializer
