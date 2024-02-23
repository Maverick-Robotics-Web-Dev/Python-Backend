from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializer import *


class LoginViewSet(TokenObtainPairView):

    serializer_class = CustomJwtTokenSerializer

    def post(self, request):

        username = request.data.get(
            'user_employee_user_name', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = UserLoginSerializer(user).data
                access = login_serializer.validated_data['access']
                refresh = login_serializer.validated_data['refresh']
                data = {'msg': 'OK', 'access': access,
                        'refresh': refresh, 'user': user_serializer}
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
