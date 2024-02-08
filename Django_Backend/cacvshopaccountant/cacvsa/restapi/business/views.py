from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.status import *

from .models import *
from .serializers import *


class WayToPayViewSet(GenericViewSet):
    model = WayToPayModel
    serializer_class = WayToPaySerializer

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            return self.model.objects.filter(way_to_pay_status=True)
        return self.queryset

    def list(self, request):
        print(request)
        waytopays = self.get_queryset()
        serializer = self.serializer_class(waytopays, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def retrieve(self, request, pk=None):
        print(pk)
        waytopays = self.get_object(pk)
        serializer = self.serializer_class(waytopays)
        data = {'data': serializer.data}
        return Response(data, HTTP_200_OK)

    def create(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'message': 'OK', 'data': serializer.data}
            return Response(data, status=HTTP_201_CREATED)
        data = {'msg': 'Error', 'errors': serializer.errors}
        return Response(data, status=HTTP_400_BAD_REQUEST)


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
