from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


class WayToPayAPIView(APIView):

    def get(self,request):
        waytopays=WayToPayModel.objects.all()
        waytopays_serializer=WayToPaySerializer(waytopays,many=True)
        return Response(waytopays_serializer.data)


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
