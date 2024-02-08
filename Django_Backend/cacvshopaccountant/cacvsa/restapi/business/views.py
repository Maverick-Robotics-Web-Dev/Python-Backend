from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.status import *

from .models import *
from .serializers import *


class WayToPayViewSet(GenericViewSet):
    model = WayToPayModel
    serializer_class = WayToPaySerializer

    def get_queryset(self):
        if self.queryset is None:
            return self.model.objects.all()
        return self.queryset

    def list(self, request):
        waytopays = self.get_queryset()
        serializer = self.serializer_class(waytopays, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

# class VoucherTypeViewSet(viewsets.ModelViewSet):
#     queryset = VoucherTypeModel.objects.all()
#     # permission_classes = [AllowAny]
#     serializer_class = VoucherTypeSerializer


# class CreditNoteViewSet(viewsets.ModelViewSet):
#     queryset = VoucherTypeModel.objects.all()
#     # permission_classes = [AllowAny]
#     serializer_class = CreditNoteSerializaer


# class CreditNoteDetailViewSet(viewsets.ModelViewSet):
#     queryset = VoucherTypeModel.objects.all()
#     # permission_classes = [AllowAny]
#     serializer_class = CreditNoteDetailSerializer


# class SaleViewSet(viewsets.ModelViewSet):
#     queryset = VoucherTypeModel.objects.all()
#     # permission_classes = [AllowAny]
#     serializer_class = SaleSerializer


# class SaleDetailViewSet(viewsets.ModelViewSet):
#     queryset = VoucherTypeModel.objects.all()
#     # permission_classes = [AllowAny]
#     serializer_class = SaleDetailSerializer
