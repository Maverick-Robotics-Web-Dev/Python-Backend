from typing import Self
from datetime import datetime

from django.db.models.query import QuerySet
from django.contrib.auth.hashers import make_password

from rest_framework.serializers import Serializer
from rest_framework.request import Request
from rest_framework.response import Response
# from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT
)

from restapi.support.views import MultiSerializerViewSet

from .models import (
    UserLevelModel,
    UserEmployeeModel,
    UserClientModel
)
from .serializers import (
    UserLevelSerializer,
    UserLevelRelatedSerializer,
    UserSudoSerializer,
    UserSudoRelatedSerializer,
    UserEmployeeSerializer,
    UserEmployeeRelatedSerializer,
    UserClientSerializer,
    UserClientRelatedSerializer
)


class UserLevelViewSet(MultiSerializerViewSet):

    model = UserLevelModel
    serializers: dict = None
    obj: UserLevelModel = None
    query_res: QuerySet = None
    serializer: Serializer = None
    data: dict = None
    response_error: ValidationError = None
    response: Response = None

    model = UserLevelModel
    serializers = {
        'default': UserLevelSerializer,
        'list': UserLevelRelatedSerializer,
        'retrieve': UserLevelRelatedSerializer
    }

    def get_object(self: Self, pk: str) -> UserLevelModel:

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


class UserSudoViewSet(MultiSerializerViewSet):

    model = UserEmployeeModel
    serializers: dict = None
    obj: UserEmployeeModel = None
    query_res: QuerySet = None
    serializer: Serializer = None
    data: dict = None
    response_error: ValidationError = None
    response: Response = None

    model = UserEmployeeModel
    serializers = {
        'default': UserSudoSerializer,
        'list': UserSudoRelatedSerializer,
        'retrieve': UserSudoRelatedSerializer
    }

    def get_object(self: Self, pk: str) -> UserEmployeeModel:

        try:

            self.obj = self.model.objects.get(pk=pk, status=True, is_active=True)
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
            return self.model.objects.filter(status=True, is_active=True)

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

        request.data["password"] = make_password(request.data["password"])
        request.data["status"] = True
        request.data["is_superuser"] = True
        request.data["is_staff"] = True
        request.data["is_active"] = True
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
        request.data["is_active"] = False
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


class UserEmployeeViewSet(MultiSerializerViewSet):

    model = UserEmployeeModel
    serializers: dict = None
    obj: UserEmployeeModel = None
    query_res: QuerySet = None
    serializer: Serializer = None
    data: dict = None
    response_error: ValidationError = None
    response: Response = None

    model = UserEmployeeModel
    serializers = {
        'default': UserEmployeeSerializer,
        'list': UserEmployeeRelatedSerializer,
        'retrieve': UserEmployeeRelatedSerializer
    }

    def get_object(self: Self, pk: str) -> UserEmployeeModel:

        try:

            self.obj = self.model.objects.get(pk=pk, status=True, is_active=True)
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
            return self.model.objects.filter(status=True, is_active=True)

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

        request.data["password"] = make_password(request.data["password"])
        request.data["status"] = True
        request.data["is_superuser"] = False
        request.data["is_staff"] = True
        request.data["is_active"] = True
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
        request.data["is_active"] = False
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


class UserClientViewSet(MultiSerializerViewSet):

    model = UserClientModel
    serializers: dict = None
    obj: UserClientModel = None
    query_res: QuerySet = None
    serializer: Serializer = None
    data: dict = None
    response_error: ValidationError = None
    response: Response = None

    model = UserClientModel
    serializers = {
        'default': UserClientSerializer,
        'list': UserClientRelatedSerializer,
        'retrieve': UserClientRelatedSerializer
    }

    def get_object(self: Self, pk: str) -> UserClientModel:

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

        request.data["password"] = make_password(request.data["password"])
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
