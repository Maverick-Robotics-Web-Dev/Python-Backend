from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.status import *

from .models import *
from .serializers import *


class CashRegisterViewSet(GenericViewSet):

    model = CashRegisterModel
    serializer_class = CashRegisterSerializer

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):

        if self.queryset is None:
            return self.model.objects.filter(cash_register_status=True)

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

        request.data['cash_register_status'] = True
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

        request.data['cash_register_update_at'] = datetime.now().strftime(
            '%B %d, %Y - %H:%M:%S')
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
            cash_register_id=pk).update(cash_register_status=False)

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


class CashRegisterOpeningViewSet(GenericViewSet):

    model = CashRegisterOpeningModel
    serializer_class = CashRegisterOpeningSerializer

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


class CashRegisterMovementsViewSet(GenericViewSet):

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


class CashRegisterClosingViewSet(GenericViewSet):

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
