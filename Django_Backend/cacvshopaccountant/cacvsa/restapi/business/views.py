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

    model = VoucherTypeModel
    serializers = {
        'default': VoucherTypeSerializer,
        'list': VoucherTypeRelatedSerializer,
        'retrieve': VoucherTypeRelatedSerializer
    }

    def get_object(self: Self, pk: str) -> VoucherTypeModel:

        try:

            obj: VoucherTypeModel = None

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
        serializer: VoucherTypeRelatedSerializer = None
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

        queryres: VoucherTypeModel = None
        serializer: VoucherTypeRelatedSerializer = None
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

        serializer: VoucherTypeSerializer = None
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

        queryres: VoucherTypeModel = None
        serializer: VoucherTypeSerializer = None
        data: dict = None
        response: Response = None

        request.data["update_at"] = datetime.now()

        queryres = self.get_object(pk)
        serializer = self.get_serializer(
            queryres, data=request.data, partial=True)

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

        queryres: VoucherTypeModel = None
        serializer: VoucherTypeSerializer = None
        data: dict = None
        response: Response = None

        request.data["status"] = False
        request.data["update_at"] = datetime.now()

        queryres = self.get_object(pk)
        serializer = self.get_serializer(
            queryres, data=request.data, partial=True)

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


class CreditNoteViewSet(MultiSerializerViewSet):

    model: CreditNoteModel = None
    serializers: dict = None

    model = CreditNoteModel
    serializers = {
        'default': CreditNoteSerializer,
        'list': CreditNoteRelatedSerializer,
        'retrieve': CreditNoteRelatedSerializer
    }

    def get_object(self: Self, pk: str) -> CreditNoteModel:

        try:

            obj: CreditNoteModel = None

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
        serializer: CreditNoteRelatedSerializer = None
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

        queryres: CreditNoteModel = None
        serializer: CreditNoteRelatedSerializer = None
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

        serializer: CreditNoteSerializer = None
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

        queryres: CreditNoteModel = None
        serializer: CreditNoteSerializer = None
        data: dict = None
        response: Response = None

        request.data["update_at"] = datetime.now()

        queryres = self.get_object(pk)
        serializer = self.get_serializer(
            queryres, data=request.data, partial=True)

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

        queryres: CreditNoteModel = None
        serializer: CreditNoteSerializer = None
        data: dict = None
        response: Response = None

        request.data["status"] = False
        request.data["update_at"] = datetime.now()

        queryres = self.get_object(pk)
        serializer = self.get_serializer(
            queryres, data=request.data, partial=True)

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


class CreditNoteDetailViewSet(MultiSerializerViewSet):

    model: CreditNoteDetailModel = None
    serializers: dict = None

    model = CreditNoteDetailModel
    serializers = {
        'default': CreditNoteDetailSerializer,
        'list': CreditNoteDetailRelatedSerializer,
        'retrieve': CreditNoteDetailRelatedSerializer
    }

    def get_object(self: Self, pk: str) -> CreditNoteDetailModel:

        try:

            obj: CreditNoteDetailModel = None

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
        serializer: CreditNoteDetailRelatedSerializer = None
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

        queryres: CreditNoteDetailModel = None
        serializer: CreditNoteDetailRelatedSerializer = None
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

        serializer: CreditNoteDetailSerializer = None
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

        queryres: CreditNoteDetailModel = None
        serializer: CreditNoteDetailSerializer = None
        data: dict = None
        response: Response = None

        request.data["update_at"] = datetime.now()

        queryres = self.get_object(pk)
        serializer = self.get_serializer(
            queryres, data=request.data, partial=True)

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

        queryres: CreditNoteDetailModel = None
        serializer: CreditNoteDetailSerializer = None
        data: dict = None
        response: Response = None

        request.data["status"] = False
        request.data["update_at"] = datetime.now()

        queryres = self.get_object(pk)
        serializer = self.get_serializer(
            queryres, data=request.data, partial=True)

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


class SaleViewSet(MultiSerializerViewSet):

    model: SaleModel = None
    serializers: dict = None

    model = SaleModel
    serializers = {
        'default': SaleSerializer,
        'list': SaleRelatedSerializer,
        'retrieve': SaleRelatedSerializer
    }

    def get_object(self: Self, pk: str) -> SaleModel:

        try:

            obj: SaleModel = None

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
        serializer: SaleRelatedSerializer = None
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

        queryres: SaleModel = None
        serializer: SaleRelatedSerializer = None
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

        serializer: SaleSerializer = None
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

        queryres: SaleModel = None
        serializer: SaleSerializer = None
        data: dict = None
        response: Response = None

        request.data["update_at"] = datetime.now()

        queryres = self.get_object(pk)
        serializer = self.get_serializer(
            queryres, data=request.data, partial=True)

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

        queryres: SaleModel = None
        serializer: SaleSerializer = None
        data: dict = None
        response: Response = None

        request.data["status"] = False
        request.data["update_at"] = datetime.now()

        queryres = self.get_object(pk)
        serializer = self.get_serializer(
            queryres, data=request.data, partial=True)

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


class SaleDetailViewSet(MultiSerializerViewSet):

    model: SaleDetailModel = None
    serializers: dict = None

    model = SaleDetailModel
    serializers = {
        'default': SaleDetailSerializer,
        'list': SaleDetailRelatedSerializer,
        'retrieve': SaleDetailRelatedSerializer
    }

    def get_object(self: Self, pk: str) -> SaleDetailModel:

        try:

            obj: SaleDetailModel = None

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
        serializer: SaleDetailRelatedSerializer = None
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

        queryres: SaleDetailModel = None
        serializer: SaleDetailRelatedSerializer = None
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

        serializer: SaleDetailSerializer = None
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

        queryres: SaleDetailModel = None
        serializer: SaleDetailSerializer = None
        data: dict = None
        response: Response = None

        request.data["update_at"] = datetime.now()

        queryres = self.get_object(pk)
        serializer = self.get_serializer(
            queryres, data=request.data, partial=True)

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

        queryres: SaleDetailModel = None
        serializer: SaleDetailSerializer = None
        data: dict = None
        response: Response = None

        request.data["status"] = False
        request.data["update_at"] = datetime.now()

        queryres = self.get_object(pk)
        serializer = self.get_serializer(
            queryres, data=request.data, partial=True)

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
