from datetime import datetime
from typing import Self
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import GenericViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework import exceptions

from .models import *
from .serializers import *


class UserLevelViewSet(GenericViewSet):

    model = UserLevelModel
    serializer_class = UserLevelSerializer

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            return self.model.objects.filter(user_level_status=True)
        return self.queryset

    def list(self, request):

        queryres = self.get_queryset()
        serializer = self.serializer_class(queryres, many=True)
        data = {'msg': 'OK', 'data': serializer.data}
        return Response(data, HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryres = self.get_object(pk)
        serializer = self.serializer_class(queryres)
        data = {'msg': 'OK', 'data': serializer.data}
        return Response(data, HTTP_200_OK)

    def create(self, request):
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

    def destroy(self, request, pk=None):
        queryres = self.model.objects.filter(
            user_level_id=pk).update(user_level_status=False)
        if queryres == 1:
            data = {'msg': 'OK'}
            return Response(data, HTTP_200_OK)
        data = {'msg': 'ERROR'}
        return Response(data, HTTP_404_NOT_FOUND)


class UserEmployeeViewSet(GenericViewSet):

    model = UserEmployeeModel
    serializer_class = UserEmployeeSerializer

    def get_object(self, pk):

        try:
            obj = self.model.objects.get(pk=pk,
                                         user_employee_status=True, is_active=True)
            return obj
        except self.model.DoesNotExist:
            data = {'error': 'ERROR', 'msg': 'No existe'}
            raise exceptions.ValidationError(data)

    def get_queryset(self):
        if self.queryset is None:
            return self.model.objects.filter(is_active=True)
        return self.queryset

    def list(self: Self, request: Request):
        queryres = self.get_queryset()
        serializer = self.serializer_class(queryres, many=True)
        data = {'msg': 'OK', 'data': serializer.data}
        return Response(data, HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryres = self.get_object(pk)
        serializer = self.serializer_class(queryres)
        data = {'msg': 'OK', 'data': serializer.data}
        return Response(data, HTTP_200_OK)

    def create(self, request):
        request.data["password"] = make_password(request.data["password"])
        request.data["user_employee_status"] = True
        request.data["is_active"] = True
        request.data["user_employee_create_at"] = datetime.now()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'msg': 'OK', 'data': serializer.data}
            return Response(data, HTTP_201_CREATED)
        data = {'msg': 'ERROR', 'errors': serializer.errors}
        return Response(data, HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):

        request.data["user_employee_update_at"] = datetime.now()
        queryres = self.get_object(pk)

        serializer = self.serializer_class(
            queryres, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {'msg': 'OK', 'data': serializer.data}
            return Response(data, HTTP_201_CREATED)
        data = {'msg': 'ERROR', 'errors': serializer.errors}
        return Response(data, HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        request.data["user_employee_status"] = False
        request.data["is_active"] = False
        request.data["user_employee_update_at"] = datetime.now()
        queryres = self.get_object(pk)
        serializer = self.serializer_class(
            queryres, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {'msg': 'OK'}
            return Response(data, HTTP_200_OK)
        data = {'msg': 'ERROR', 'errors': serializer.errors}
        return Response(data, HTTP_204_NO_CONTENT)


class UserClientViewSet(GenericViewSet):

    model = UserClientModel
    serializer_class = UserClientSerializer

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):

        if self.queryset is None:
            return self.model.objects.filter(user_client_status=True)
        return self.queryset

    def list(self, request):

        queryres = self.get_queryset()
        serializer = self.serializer_class(queryres, many=True)
        data = {'msg': 'OK', 'data': serializer.data}
        return Response(data, HTTP_200_OK)

    def retrieve(self, request, pk=None):

        queryres = self.get_object(pk)
        serializer = self.serializer_class(queryres)
        data = {'msg': 'OK', 'data': serializer.data}
        return Response(data, HTTP_200_OK)

    def create(self, request):

        request.data["password"] = make_password(request.data["password"])
        request.data["user_client_status"] = True
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

    def destroy(self, request, pk=None):
        queryres = self.model.objects.filter(
            user_client_id=pk).update(user_client_status=False)
        if queryres == 1:
            data = {'msg': 'OK'}
            return Response(data, HTTP_200_OK)
        data = {'msg': 'ERROR'}
        return Response(data, HTTP_404_NOT_FOUND)
