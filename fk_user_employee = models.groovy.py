from datetime import datetime
from typing import Self

from restapi.abstracts.models import NestedModel

from django.db.models.query import QuerySet

from rest_framework.serializers import (
    ModelSerializer,
    StringRelatedField
)

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


fk_user_employee = ForeignKey('users.UserEmployeeModel', on_delete=models.CASCADE, verbose_name='Usuario')

        db_table: str = None
        verbose_name: str = None
        verbose_name_plural: str = None

def __str__(self: Self) -> LiteralString:
        return self.name

fk_user_employee = StringRelatedField()
default='No existe descripción'

->
Related
models.BooleanField('Estado', default=False)

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

        queryres: QuerySet = None
        serializer: WayToPayRelatedSerializer = None
        data: dict = None
        response: Response = None

        queryres = self.get_queryset()
        serializer = self.get_serializer(queryres, many=True)

        data = {
            'ok': 'OK',
            'data': serializer.data
        }

        response = Response(data, HTTP_200_OK)

        return response

    def retrieve(self: Self, request: Request, pk: str = None):

        queryres: WayToPayModel = None
        serializer: WayToPayRelatedSerializer = None
        data: dict = None
        response: Response = None

        queryres = self.get_object(pk)
        serializer = self.get_serializer(queryres)

        data = {
            'ok': 'OK',
            'data': serializer.data
        }

        response = Response(data, HTTP_200_OK)

        return response

    def create(self: Self, request: Request):

        serializer: WayToPaySerializer = None
        data: dict = None
        response: Response = None

        request.data["status"] = True
        request.data["create_at"] = datetime.now()

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            data = {
                'ok': 'OK',
                'msg': 'Creado Exitosamente',
                'data': serializer.data
            }

            response = Response(data, HTTP_201_CREATED)

            return response

        data = {
            'error': 'ERROR',
            'msg': serializer.errors
        }

        response = Response(data, HTTP_400_BAD_REQUEST)

        return response

    def partial_update(self: Self, request: Request, pk: str = None):

        queryres: WayToPayModel = None
        serializer: WayToPaySerializer = None
        data: dict = None
        response: Response = None

        request.data["update_at"] = datetime.now()

        queryres = self.get_object(pk)
        serializer = self.get_serializer(queryres, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            data = {
                'ok': 'OK',
                'msg': 'Actualizado Exitosamente',
                'data': serializer.data
            }

            response = Response(data, HTTP_201_CREATED)

            return response

        data = {
            'error': 'ERROR',
            'msg': serializer.errors
        }

        response = Response(data, HTTP_400_BAD_REQUEST)

        return response

    def destroy(self: Self, request: Request, pk: str = None):

        queryres: WayToPayModel = None
        serializer: WayToPaySerializer = None
        data: dict = None
        response: Response = None

        request.data["status"] = False
        request.data["update_at"] = datetime.now()

        queryres = self.get_object(pk)
        serializer = self.get_serializer(queryres, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            data = {
                'ok': 'OK',
                'msg': 'Eliminado Exitosamente',
            }

            response = Response(data, HTTP_200_OK)

            return response

        data = {
            'error': 'ERROR',
            'msg': serializer.errors
        }

        response = Response(data, HTTP_400_BAD_REQUEST)

        return response