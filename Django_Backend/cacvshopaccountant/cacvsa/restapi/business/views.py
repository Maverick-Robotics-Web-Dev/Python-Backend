from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.status import *

from cacvsa.settings.base import *
from .models import *
from .serializers import *
from restapi.mixins.usermixins import *


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

        queryres = self.get_queryset()
        serializer = self.serializer_class(queryres, many=True)

        response = {
            'ok': 'OK',
            'data': serializer.data
        }

        return Response(response, HTTP_200_OK)

    def retrieve(self, request, pk=None):

        queryres = self.get_object(pk)
        serializer = self.serializer_class(queryres)

        response = {
            'ok': 'OK',
            'data': serializer.data
        }

        return Response(response, HTTP_200_OK)

    def create(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            response = {
                'ok': 'OK',
                'msg': 'Creado Exitosamente',
                'data': serializer.data
            }

            return Response(response, HTTP_201_CREATED)

        response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }

        return Response(response, HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):

        queryres = self.get_object(pk)
        serializer = self.serializer_class(
            queryres, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            response = {
                'ok': 'OK',
                'msg': 'Actualizado Exitosamente',
                'data': serializer.data
            }

            return Response(response, HTTP_201_CREATED)

        response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }

        return Response(response, HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):

        queryres = self.model.objects.filter(
            way_to_pay_id=pk).update(way_to_pay_status=False)

        if queryres == 1:

            response = {
                'ok': 'OK',
                'msg': 'Eliminado Exitosamente'
            }

            return Response(response, HTTP_200_OK)

        response = {
            'error': 'ERROR',
            'msg': 'No existe'
        }

        return Response(response, HTTP_404_NOT_FOUND)


class VoucherTypeViewSet(GenericViewSet):

    model = VoucherTypeModel
    serializer_class = VoucherTypeSerializer

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):

        if self.queryset is None:
            return self.model.objects.filter(voucher_type_status=True)

        return self.queryset

    def list(self, request):

        queryres = self.get_queryset()
        serializer = self.serializer_class(queryres, many=True)

        response = {
            'ok': 'OK',
            'data': serializer.data
        }

        return Response(response, HTTP_200_OK)

    def retrieve(self, request, pk=None):

        queryres = self.get_object(pk)
        serializer = self.serializer_class(queryres)

        response = {
            'ok': 'OK',
            'data': serializer.data
        }

        return Response(response, HTTP_200_OK)

    def create(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            response = {
                'ok': 'OK',
                'msg': 'Creado Exitosamente',
                'data': serializer.data
            }

            return Response(response, HTTP_201_CREATED)

        response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }

        return Response(response, HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):

        queryres = self.get_object(pk)
        serializer = self.serializer_class(
            queryres, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            response = {
                'ok': 'OK',
                'msg': 'Actualizado Exitosamente',
                'data': serializer.data
            }

            return Response(response, HTTP_201_CREATED)

        response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }

        return Response(response, HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):

        queryres = self.model.objects.filter(
            voucher_type_id=pk).update(voucher_type_status=False)

        if queryres == 1:

            response = {
                'ok': 'OK',
                'msg': 'Eliminado Exitosamente',
            }

            return Response(response, HTTP_200_OK)

        response = {
            'error': 'ERROR',
            'msg': 'No existe'
        }

        return Response(response, HTTP_404_NOT_FOUND)


class CreditNoteViewSet(GenericViewSet):

    model = CreditNoteModel
    serializer_class = CreditNoteSerializaer

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):

        if self.queryset is None:
            return self.model.objects.filter(credit_note_status=True)

        return self.queryset

    def list(self, request):

        queryres = self.get_queryset()
        serializer = self.serializer_class(queryres, many=True)

        response = {
            'ok': 'OK',
            'data': serializer.data
        }

        return Response(response, HTTP_200_OK)

    def retrieve(self, request, pk=None):

        queryres = self.get_object(pk)
        serializer = self.serializer_class(queryres)

        response = {
            'ok': 'OK',
            'data': serializer.data
        }

        return Response(response, HTTP_200_OK)

    def create(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            response = {
                'ok': 'OK',
                'msg': 'Creado Exitosamente',
                'data': serializer.data
            }

            return Response(response, HTTP_201_CREATED)

        response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }

        return Response(response, HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):

        queryres = self.get_object(pk)
        serializer = self.serializer_class(
            queryres, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            response = {
                'ok': 'OK',
                'msg': 'Actualizado Exitosamente',
                'data': serializer.data
            }

            return Response(response, HTTP_201_CREATED)

        response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }

        return Response(response, HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):

        queryres = self.model.objects.filter(
            credit_note_id=pk).update(credit_note_status=False)

        if queryres == 1:

            response = {
                'ok': 'OK',
                'msg': 'Eliminado Exitosamente',
            }

            return Response(response, HTTP_200_OK)

        response = {
            'error': 'ERROR',
            'msg': 'No existe'
        }

        return Response(response, HTTP_404_NOT_FOUND)


class CreditNoteDetailViewSet(GenericViewSet):

    model = CreditNoteDetailModel
    serializer_class = CreditNoteDetailSerializer

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):

        if self.queryset is None:
            return self.model.objects.all()

        return self.queryset

    def list(self, request):

        queryres = self.get_queryset()
        serializer = self.serializer_class(queryres, many=True)

        response = {
            'ok': 'OK',
            'data': serializer.data
        }

        return Response(response, HTTP_200_OK)

    def retrieve(self, request, pk=None):

        queryres = self.get_object(pk)
        serializer = self.serializer_class(queryres)

        response = {
            'ok': 'OK',
            'data': serializer.data
        }

        return Response(response, HTTP_200_OK)

    def create(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            response = {
                'ok': 'OK',
                'msg': 'Creado Exitosamente',
                'data': serializer.data
            }

            return Response(response, HTTP_201_CREATED)

        response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }

        return Response(response, HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):

        queryres = self.get_object(pk)
        serializer = self.serializer_class(
            queryres, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            response = {
                'ok': 'OK',
                'msg': 'Actualizado Exitosamente',
                'data': serializer.data
            }

            return Response(response, HTTP_201_CREATED)

        response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }

        return Response(response, HTTP_400_BAD_REQUEST)


class SaleViewSet(GenericViewSet):

    model = SaleModel
    serializer_class = SaleSerializer

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):

        if self.queryset is None:
            return self.model.objects.filter(sale_status=True)

        return self.queryset

    def list(self, request):

        queryres = self.get_queryset()
        serializer = self.serializer_class(queryres, many=True)

        response = {
            'ok': 'OK',
            'data': serializer.data
        }

        return Response(response, HTTP_200_OK)

    def retrieve(self, request, pk=None):

        queryres = self.get_object(pk)
        serializer = self.serializer_class(queryres)

        response = {
            'ok': 'OK',
            'data': serializer.data
        }

        return Response(response, HTTP_200_OK)

    def create(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            response = {
                'ok': 'OK',
                'msg': 'Creado Exitosamente',
                'data': serializer.data
            }

            return Response(response, HTTP_201_CREATED)

        response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }

        return Response(response, HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):

        queryres = self.get_object(pk)
        serializer = self.serializer_class(
            queryres, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            response = {
                'ok': 'OK',
                'msg': 'Actualizado Exitosamente',
                'data': serializer.data
            }

            return Response(response, HTTP_201_CREATED)

        response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }

        return Response(response, HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):

        queryres = self.model.objects.filter(
            sale_id=pk).update(sale_status=False)

        if queryres == 1:

            response = {
                'ok': 'OK',
                'msg': 'Eliminado Exitosamente',
            }

            return Response(response, HTTP_200_OK)

        response = {
            'error': 'ERROR',
            'msg': 'No existe'
        }

        return Response(response, HTTP_404_NOT_FOUND)


class SaleDetailViewSet(GenericViewSet):

    model = SaleDetailModel
    serializer_class = SaleDetailSerializer

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):

        if self.queryset is None:
            return self.model.objects.all()

        return self.queryset

    def list(self, request):

        queryres = self.get_queryset()
        serializer = self.serializer_class(queryres, many=True)

        response = {
            'ok': 'OK',
            'data': serializer.data
        }

        return Response(response, HTTP_200_OK)

    def retrieve(self, request, pk=None):

        queryres = self.get_object(pk)
        serializer = self.serializer_class(queryres)

        response = {
            'ok': 'OK',
            'data': serializer.data
        }

        return Response(response, HTTP_200_OK)

    def create(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            response = {
                'ok': 'OK',
                'msg': 'Creado Exitosamente',
                'data': serializer.data
            }

            return Response(response, HTTP_201_CREATED)

        response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }

        return Response(response, HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):

        queryres = self.get_object(pk)
        serializer = self.serializer_class(
            queryres, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            response = {
                'ok': 'OK',
                'msg': 'Actualizado Exitosamente',
                'data': serializer.data
            }

            return Response(response, HTTP_201_CREATED)

        response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }

        return Response(response, HTTP_400_BAD_REQUEST)
