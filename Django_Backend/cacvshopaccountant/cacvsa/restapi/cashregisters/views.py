from typing import Self
from datetime import datetime

from django.db.models.query import QuerySet

from rest_framework.serializers import Serializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT
)

from restapi.support.views import MultiSerializerViewSet

from .models import (
    CashRegisterModel,
    CashRegisterOpeningModel,
    CashRegisterMovementsModel,
    CashRegisterClosingModel
)

from .serializers import (
    CashRegisterSerializer,
    CashRegisterRelatedSerializer,
    CashRegisterOpeningSerializer,
    CashRegisterOpeningRelatedSerializer,
    CashRegisterMovementsSerializer,
    CashRegisterMovementsRelatedSerializer,
    CashRegisterClosingSerializer,
    CashRegisterClosingRelatedSerializer
)


class CashRegisterViewSet(MultiSerializerViewSet):

    model = CashRegisterModel
    serializers: dict = None
    obj: CashRegisterModel = None
    query_res: QuerySet = None
    serializer: Serializer = None
    data: dict = None
    response_error: ValidationError = None
    response: Response = None

    model = CashRegisterModel
    serializers = {
        'default': CashRegisterSerializer,
        'list': CashRegisterRelatedSerializer,
        'retrieve': CashRegisterRelatedSerializer
    }

    def get_object(self: Self, pk: str) -> CashRegisterModel:

        try:

            self.obj = self.model.objects.get(pk=pk, status=True)
            return self.obj

        except self.model.DoesNotExist:

            self.data = {
                'error': 'ERROR',
                'msg': 'No existe'
            }

            self.response_error = ValidationError(self.data, HTTP_204_NO_CONTENT)

            raise self.response_error

    def get_queryset(self: Self) -> QuerySet:

        if self.queryset is None:
            return self.model.objects.filter(status=True)

        return self.queryset

    def list(self: Self, request: Request) -> Response:

        self.query_res = self.get_queryset()
        self.serializer = self.get_serializer(self.query_res, many=True)

        self.data = {
            'ok': 'OK',
            'data': self.serializer.data
        }

        self.response = Response(self.data, HTTP_200_OK)

        return self.response

    def retrieve(self: Self, request: Request, pk: str = None):

        self.obj = self.get_object(pk)
        self.serializer = self.get_serializer(self.obj)

        self.data = {
            'ok': 'OK',
            'data': self.serializer.data
        }

        self.response = Response(self.data, HTTP_200_OK)

        return self.response

    def create(self: Self, request: Request):

        request.data["status"] = True
        request.data["create_at"] = datetime.now()

        self.serializer = self.get_serializer(data=request.data)

        if self.serializer.is_valid():

            self.serializer.save()

            self.data = {
                'ok': 'OK',
                'msg': 'Creado Exitosamente',
                'data': self.serializer.data
            }

            self.response = Response(self.data, HTTP_201_CREATED)

            return self.response

        self.data = {
            'error': 'ERROR',
            'msg': self.serializer.errors
        }

        self.response = Response(self.data, HTTP_400_BAD_REQUEST)

        return self.response

    def partial_update(self: Self, request: Request, pk: str = None):

        request.data["update_at"] = datetime.now()

        self.obj = self.get_object(pk)
        self.serializer = self.get_serializer(self.obj, data=request.data, partial=True)

        if self.serializer.is_valid():

            self.serializer.save()

            self.data = {
                'ok': 'OK',
                'msg': 'Actualizado Exitosamente',
                'data': self.serializer.data
            }

            self.response = Response(self.data, HTTP_201_CREATED)

            return self.response

        self.data = {
            'error': 'ERROR',
            'msg': self.serializer.errors
        }

        self.response = Response(self.data, HTTP_400_BAD_REQUEST)

        return self.response

    def destroy(self: Self, request: Request, pk: str = None):

        request.data["status"] = False
        request.data["update_at"] = datetime.now()

        self.obj = self.get_object(pk)
        self.serializer = self.get_serializer(self.obj, data=request.data, partial=True)

        if self.serializer.is_valid():

            self.serializer.save()

            self.data = {
                'ok': 'OK',
                'msg': 'Eliminado Exitosamente',
            }

            self.response = Response(self.data, HTTP_200_OK)

            return self.response

        self.data = {
            'error': 'ERROR',
            'msg': self.serializer.errors
        }

        self.response = Response(self.data, HTTP_400_BAD_REQUEST)

        return self.response


class CashRegisterOpeningViewSet(MultiSerializerViewSet):

    model = CashRegisterOpeningModel
    serializers: dict = None
    obj: CashRegisterOpeningModel = None
    query_res: QuerySet = None
    serializer: Serializer = None
    data: dict = None
    response_error: ValidationError = None
    response: Response = None

    model = CashRegisterOpeningModel
    serializers = {
        'default': CashRegisterOpeningSerializer,
        'list': CashRegisterOpeningRelatedSerializer,
        'retrieve': CashRegisterOpeningRelatedSerializer
    }

    def get_object(self: Self, pk: str) -> CashRegisterOpeningModel:

        try:

            self.obj = self.model.objects.get(pk=pk, status=True)
            return self.obj

        except self.model.DoesNotExist:

            self.data = {
                'error': 'ERROR',
                'msg': 'No existe'
            }

            self.response_error = ValidationError(self.data, HTTP_204_NO_CONTENT)

            raise self.response_error

    def get_queryset(self: Self) -> QuerySet:

        if self.queryset is None:
            return self.model.objects.filter(status=True)

        return self.queryset

    def list(self: Self, request: Request) -> Response:

        self.query_res = self.get_queryset()
        self.serializer = self.get_serializer(self.query_res, many=True)

        self.data = {
            'ok': 'OK',
            'data': self.serializer.data
        }

        self.response = Response(self.data, HTTP_200_OK)

        return self.response

    def retrieve(self: Self, request: Request, pk: str = None):

        self.obj = self.get_object(pk)
        self.serializer = self.get_serializer(self.obj)

        self.data = {
            'ok': 'OK',
            'data': self.serializer.data
        }

        self.response = Response(self.data, HTTP_200_OK)

        return self.response

    def create(self: Self, request: Request):

        request.data["status"] = True
        request.data["create_at"] = datetime.now()

        self.serializer = self.get_serializer(data=request.data)

        if self.serializer.is_valid():

            self.serializer.save()

            self.data = {
                'ok': 'OK',
                'msg': 'Creado Exitosamente',
                'data': self.serializer.data
            }

            self.response = Response(self.data, HTTP_201_CREATED)

            return self.response

        self.data = {
            'error': 'ERROR',
            'msg': self.serializer.errors
        }

        self.response = Response(self.data, HTTP_400_BAD_REQUEST)

        return self.response

    def partial_update(self: Self, request: Request, pk: str = None):

        request.data["update_at"] = datetime.now()

        self.obj = self.get_object(pk)
        self.serializer = self.get_serializer(self.obj, data=request.data, partial=True)

        if self.serializer.is_valid():

            self.serializer.save()

            self.data = {
                'ok': 'OK',
                'msg': 'Actualizado Exitosamente',
                'data': self.serializer.data
            }

            self.response = Response(self.data, HTTP_201_CREATED)

            return self.response

        self.data = {
            'error': 'ERROR',
            'msg': self.serializer.errors
        }

        self.response = Response(self.data, HTTP_400_BAD_REQUEST)

        return self.response

    def destroy(self: Self, request: Request, pk: str = None):

        request.data["status"] = False
        request.data["update_at"] = datetime.now()

        self.obj = self.get_object(pk)
        self.serializer = self.get_serializer(self.obj, data=request.data, partial=True)

        if self.serializer.is_valid():

            self.serializer.save()

            self.data = {
                'ok': 'OK',
                'msg': 'Eliminado Exitosamente',
            }

            self.response = Response(self.data, HTTP_200_OK)

            return self.response

        self.data = {
            'error': 'ERROR',
            'msg': self.serializer.errors
        }

        self.response = Response(self.data, HTTP_400_BAD_REQUEST)

        return self.response


class CashRegisterMovementsViewSet(MultiSerializerViewSet):

    model = CashRegisterMovementsModel
    serializer_class = CashRegisterMovementsSerializer

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            return self.model.objects.all()
        return self.queryset

    def list(self, request):
        # print(request)
        queryres = self.get_queryset()
        serializer = self.serializer_class(queryres, many=True)
        data = {'msg': 'OK', 'data': serializer.data}
        return Response(data, HTTP_200_OK)

    def retrieve(self, request, pk=None):
        # print(pk)
        queryres = self.get_object(pk)
        serializer = self.serializer_class(queryres)
        data = {'msg': 'OK', 'data': serializer.data}
        return Response(data, HTTP_200_OK)

    def create(self, request):
        # print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'msg': 'OK', 'data': serializer.data}
            return Response(data, HTTP_201_CREATED)
        data = {'msg': 'ERROR', 'errors': serializer.errors}
        return Response(data, HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryres = self.get_object(pk)
        serializer = self.serializer_class(
            queryres, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {'msg': 'OK', 'data': serializer.data}
            return Response(data, HTTP_201_CREATED)
        data = {'msg': 'ERROR', 'errors': serializer.errors}
        return Response(data, HTTP_400_BAD_REQUEST)

    # def destroy(self, request, pk=None):
    #     queryres = self.model.objects.filter(
    #         way_to_pay_id=pk).update(way_to_pay_status=False)
    #     if queryres == 1:
    #         data = {'msg': 'OK'}
    #         return Response(data, HTTP_200_OK)
    #     data = {'msg': 'ERROR'}
    #     return Response(data, HTTP_404_NOT_FOUND)


class CashRegisterClosingViewSet(MultiSerializerViewSet):

    model = CashRegisterClosingModel
    serializer_class = CashRegisterClosingSerializer

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            return self.model.objects.all()
        return self.queryset

    def list(self, request):
        # print(request)
        queryres = self.get_queryset()
        serializer = self.serializer_class(queryres, many=True)
        data = {'msg': 'OK', 'data': serializer.data}
        return Response(data, HTTP_200_OK)

    def retrieve(self, request, pk=None):
        # print(pk)
        queryres = self.get_object(pk)
        serializer = self.serializer_class(queryres)
        data = {'msg': 'OK', 'data': serializer.data}
        return Response(data, HTTP_200_OK)

    def create(self, request):
        # print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'msg': 'OK', 'data': serializer.data}
            return Response(data, HTTP_201_CREATED)
        data = {'msg': 'ERROR', 'errors': serializer.errors}
        return Response(data, HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryres = self.get_object(pk)
        serializer = self.serializer_class(
            queryres, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {'msg': 'OK', 'data': serializer.data}
            return Response(data, HTTP_201_CREATED)
        data = {'msg': 'ERROR', 'errors': serializer.errors}
        return Response(data, HTTP_400_BAD_REQUEST)

    # def destroy(self, request, pk=None):
    #     queryres = self.model.objects.filter(
    #         way_to_pay_id=pk).update(way_to_pay_status=False)
    #     if queryres == 1:
    #         data = {'msg': 'OK'}
    #         return Response(data, HTTP_200_OK)
    #     data = {'msg': 'ERROR'}
    #     return Response(data, HTTP_404_NOT_FOUND)
