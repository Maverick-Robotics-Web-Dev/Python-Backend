from datetime import datetime
from typing import Self

from django.db.models.query import QuerySet

from rest_framework.serializers import Serializer, ListSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_204_NO_CONTENT
)

from restapi.support.views import MultiSerializerViewSet

from .models import (
    WayToPayModel,
    VoucherTypeModel,
    CreditNoteModel,
    CreditNoteDetailModel,
    SaleModel,
    SaleDetailModel
)
from .serializers import (
    WayToPaySerializer,
    WayToPayRelatedSerializer,
    VoucherTypeSerializer,
    VoucherTypeRelatedSerializer,
    CreditNoteSerializaer,
    CreditNoteRelatedSerializaer,
    CreditNoteDetailSerializer,
    CreditNoteDetailRelatedSerializer,
    SaleSerializer,
    SaleRelatedSerializer,
    SaleDetailSerializer,
    SaleDetailRelatedSerializer
)


class WayToPayViewSet(MultiSerializerViewSet):

    model: WayToPayModel = None
    serializers: dict = None

    model = WayToPayModel
    serializers = {
        'default': WayToPaySerializer,
        'list': WayToPayRelatedSerializer,
        'retrieve': WayToPayRelatedSerializer
    }

    def get_object(self: Self, pk: str) -> WayToPayModel:

        try:

            obj: WayToPayModel = None

            obj = self.model.objects.get(pk=pk, status=True)
            return obj

        except self.model.DoesNotExist:

            data: dict = None
            response: ValidationError = None

            data = {
                'error': 'ERROR',
                'msg': 'No existe'
            }

            response = ValidationError(data, HTTP_204_NO_CONTENT)

            raise response

    def get_queryset(self: Self) -> QuerySet:

        if self.queryset is None:
            return self.model.objects.filter(status=True)

        return self.queryset

    def list(self: Self, request: Request) -> Response:

        serializer: ListSerializer = None
        queryres: QuerySet = None

        queryres = self.get_queryset()
        serializer = self.get_serializer(queryres, many=True)

        response = {
            'ok': 'OK',
            'data': serializer.data
        }
        return Response(response, HTTP_200_OK)

    def retrieve(self, request, pk=None):

        queryres = self.get_object(pk)
        serializer = self.get_serializer(queryres)

        response = {
            'ok': 'OK',
            'data': serializer.data
        }
        return Response(response, HTTP_200_OK)

    def create(self, request):

        request.data["status"] = True
        request.data["create_at"] = datetime.now()
        serializer = self.get_serializer(
            data=request.data)
        print(type(serializer))

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

        request.data["update_at"] = datetime.now()
        queryres = self.get_object(pk)
        serializer = self.get_serializer(
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

        request.data["status"] = False
        request.data["update_at"] = datetime.now()
        queryres = self.get_object(pk)
        serializer = self.get_serializer(
            queryres, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            response = {
                'ok': 'OK',
                'msg': 'Eliminado Exitosamente',
            }
            return Response(response, HTTP_200_OK)

        response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }
        return Response(response, HTTP_400_BAD_REQUEST)


class VoucherTypeViewSet(GenericViewSet):

    model = VoucherTypeModel
    serializer_class = VoucherTypeSerializer

    def get_object(self, pk):

        try:

            obj = self.model.objects.get(pk=pk, voucher_type_status=True)
            return obj

        except self.model.DoesNotExist:

            response = {'error': 'ERROR', 'msg': 'No existe'}
            raise exceptions.ValidationError(response)

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

        request.data['voucher_type_status'] = True
        request.data['voucher_type_create_at'] = datetime.now()
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

        request.data['voucher_type_update_at'] = datetime.now()
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
            return Response(response, HTTP_200_OK)

        response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }
        return Response(response, HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):

        request.data['voucher_type_status'] = False
        request.data['voucher_type_update_at'] = datetime.now()
        queryres = self.get_object(pk)
        serializer = self.serializer_class(
            queryres, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            response = {
                'ok': 'OK',
                'msg': 'Eliminado Exitosamente',
            }
            return Response(response, HTTP_200_OK)

        response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }
        return Response(response, HTTP_400_BAD_REQUEST)


class CreditNoteViewSet(GenericViewSet):

    model = CreditNoteModel
    serializer_class = CreditNoteSerializaer

    def get_object(self, pk):

        try:

            obj = self.model.objects.get(pk=pk, credit_note_status=True)
            return obj

        except self.model.DoesNotExist:

            response = {'error': 'ERROR', 'msg': 'No existe'}
            raise exceptions.ValidationError(response)

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

        request.data['credit_note_status'] = True
        request.data['credit_note_create_at'] = datetime.now()
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

        request.data['credit_note_update_at'] = datetime.now()
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
            return Response(response, HTTP_200_OK)

        response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }
        return Response(response, HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):

        request.data['credit_note_status'] = False
        request.data['credit_note_update_at'] = datetime.now()
        queryres = self.get_object(pk)
        serializer = self.serializer_class(
            queryres, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            response = {
                'ok': 'OK',
                'msg': 'Eliminado Exitosamente',
            }
            return Response(response, HTTP_200_OK)

        response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }
        return Response(response, HTTP_400_BAD_REQUEST)


class CreditNoteDetailViewSet(GenericViewSet):

    model = CreditNoteDetailModel
    serializer_class = CreditNoteDetailSerializer

    def get_object(self, pk):

        try:

            obj = self.model.objects.get(pk=pk, credit_note_detail_status=True)
            return obj

        except self.model.DoesNotExist:

            response = {'error': 'ERROR', 'msg': 'No existe'}
            raise exceptions.ValidationError(response)

    def get_queryset(self):

        if self.queryset is None:
            return self.model.objects.filter(credit_note_detail_status=True)

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

        request.data['credit_note_detail_status'] = True
        request.data['credit_note_detail_create_at'] = datetime.now()
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

        request.data['credit_note_detail_update_at'] = datetime.now()
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
            return Response(response, HTTP_200_OK)

        response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }
        return Response(response, HTTP_400_BAD_REQUEST)

    def desytoy(self, request, pk=None):

        request.data['credit_note_detail_status'] = False
        request.data['credit_note_detail_update_at'] = datetime.now()
        queryres = self.get_object(pk)
        serializer = self.serializer_class(
            queryres, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            response = {
                'ok': 'OK',
                'msg': 'Eliminado Exitosamente',
            }
            return Response(response, HTTP_200_OK)

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
