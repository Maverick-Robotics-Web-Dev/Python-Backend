from datetime import datetime
from typing import Self

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
    CreditNoteSerializer,
    CreditNoteRelatedSerializer,
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
    obj: WayToPayModel = None
    query_res: QuerySet = None
    serializer: Serializer = None
    data: dict = None
    response_error: ValidationError = None
    response: Response = None

    model = WayToPayModel
    serializers = {
        'default': WayToPaySerializer,
        'list': WayToPayRelatedSerializer,
        'retrieve': WayToPayRelatedSerializer
    }

    def get_object(self: Self, pk: str) -> WayToPayModel:

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


class VoucherTypeViewSet(MultiSerializerViewSet):

    model: VoucherTypeModel = None
    serializers: dict = None
    obj: VoucherTypeModel = None
    query_res: QuerySet = None
    serializer: Serializer = None
    data: dict = None
    response_error: ValidationError = None
    response: Response = None

    model = VoucherTypeModel
    serializers = {
        'default': VoucherTypeSerializer,
        'list': VoucherTypeRelatedSerializer,
        'retrieve': VoucherTypeRelatedSerializer
    }

    def get_object(self: Self, pk: str) -> VoucherTypeModel:

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


class CreditNoteViewSet(MultiSerializerViewSet):

    model: CreditNoteModel = None
    serializers: dict = None
    obj: CreditNoteModel = None
    query_res: QuerySet = None
    serializer: Serializer = None
    data: dict = None
    response_error: ValidationError = None
    response: Response = None

    model = CreditNoteModel
    serializers = {
        'default': CreditNoteSerializer,
        'list': CreditNoteRelatedSerializer,
        'retrieve': CreditNoteRelatedSerializer
    }

    def get_object(self: Self, pk: str) -> CreditNoteModel:

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
            return self.model.objects.all()

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


class CreditNoteDetailViewSet(MultiSerializerViewSet):

    model: CreditNoteDetailModel = None
    serializers: dict = None
    obj: CreditNoteDetailModel = None
    query_res: QuerySet = None
    serializer: Serializer = None
    data: dict = None
    response_error: ValidationError = None
    response: Response = None

    model = CreditNoteDetailModel
    serializers = {
        'default': CreditNoteDetailSerializer,
        'list': CreditNoteDetailRelatedSerializer,
        'retrieve': CreditNoteDetailRelatedSerializer
    }

    def get_object(self: Self, pk: str) -> CreditNoteDetailModel:

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


class SaleViewSet(MultiSerializerViewSet):

    model: SaleModel = None
    serializers: dict = None
    obj: SaleModel = None
    query_res: QuerySet = None
    serializer: Serializer = None
    data: dict = None
    response_error: ValidationError = None
    response: Response = None

    model = SaleModel
    serializers = {
        'default': SaleSerializer,
        'list': SaleRelatedSerializer,
        'retrieve': SaleRelatedSerializer
    }

    def get_object(self: Self, pk: str) -> SaleModel:

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
            return self.model.objects.all()

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


class SaleDetailViewSet(MultiSerializerViewSet):

    model: SaleDetailModel = None
    serializers: dict = None
    obj: SaleDetailModel = None
    query_res: QuerySet = None
    serializer: Serializer = None
    data: dict = None
    response_error: ValidationError = None
    response: Response = None

    model = SaleDetailModel
    serializers = {
        'default': SaleDetailSerializer,
        'list': SaleDetailRelatedSerializer,
        'retrieve': SaleDetailRelatedSerializer
    }

    def get_object(self: Self, pk: str) -> SaleDetailModel:

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
