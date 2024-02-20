from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
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
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            return self.model.objects.filter(is_active=True)
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

    def destroy(self, request, pk=None):
        queryres = self.model.objects.filter(
            id=pk).update(is_active=False)
        if queryres == 1:
            data = {'msg': 'OK'}
            return Response(data, HTTP_200_OK)
        data = {'msg': 'ERROR'}
        return Response(data, HTTP_404_NOT_FOUND)


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

    def destroy(self, request, pk=None):
        queryres = self.model.objects.filter(
            user_client_id=pk).update(user_client_status=False)
        if queryres == 1:
            data = {'msg': 'OK'}
            return Response(data, HTTP_200_OK)
        data = {'msg': 'ERROR'}
        return Response(data, HTTP_404_NOT_FOUND)


class LoginViewSet(TokenObtainPairView):

    serializer_class = CustomJwtToken

    def post(self, request):

        user_employee_user_name = request.data.get(
            'user_employee_user_name', '')
        password = request.data.get('password', '')
        user = authenticate(
            user_employee_user_name=user_employee_user_name, password=password)

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                access = login_serializer.validated_data.get('access')
                refresh = login_serializer.validated_data.get('refresh')
                # user_s = UserEmployeeSerializer(user).data
                data = {'msg': 'OK', 'access': access,
                        'refresh': refresh}
                return Response(data, HTTP_200_OK)
            data = {'error': 'ERROR'}
            return Response(data, HTTP_400_BAD_REQUEST)
        data = {'error': 'ERROR'}
        return Response(data, HTTP_400_BAD_REQUEST)


class LogoutViewSet(APIView):

    def post(self, request, *args, **kwargs):
        print(request.data.get('user', ''))
        queryres = UserEmployeeModel.objects.filter(
            id=request.data.get('user', ''))
        if queryres.exists():
            RefreshToken.for_user(queryres.first())
            data = {'msg': 'OK'}
            return Response(data, HTTP_200_OK)
        data = {'error': 'ERROR'}
        return Response(data, HTTP_400_BAD_REQUEST)
