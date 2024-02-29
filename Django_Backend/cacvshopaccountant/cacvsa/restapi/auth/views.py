from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate
from rest_framework_simplejwt.settings import api_settings as jwt_settings
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from cacvsa.settings.base import *
from restapi.support.methods import *
from .serializers import *


class LoginViewSet(GenericViewSet):

    model = UserEmployeeModel
    permission_classes = [AllowAny]
    serializer_class = CustomJwtTokenSerializer

    # @sensitive_post_parameters_m
    def create(self, request):

        username = request.data.get(
            'user_employee_user_name', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)

        if user:
            login_serializer = self.serializer_class(data=request.data)

            if login_serializer.is_valid():
                user_serializer = LoginSerializer(
                    user, data={'user_employee_login': True}, partial=True)
                if user_serializer.is_valid():
                    user_serializer.save()

                access_token = login_serializer.validated_data['access']
                refresh_token = login_serializer.validated_data['refresh']

                if CACV_KEY['SESSION_LOGIN']:
                    django_login(request, user)

                access_token_expiration = (
                    timezone.now() + jwt_settings.ACCESS_TOKEN_LIFETIME)
                refresh_token_expiration = (
                    timezone.now() + jwt_settings.REFRESH_TOKEN_LIFETIME)
                return_expiration_times = CACV_KEY['JWT_AUTH_RETURN_EXPIRATION']

                if return_expiration_times:
                    data = {
                        'msg': 'OK',
                        'access': access_token,
                        'refresh': refresh_token,
                        'access_expiration': access_token_expiration,
                        'refresh_expiration': refresh_token_expiration,
                        'user': user_serializer.data,
                    }

                data = {
                    'msg': 'OK',
                    'access': access_token,
                    'refresh': refresh_token,
                    'user': user_serializer.data
                }

                # serializer = self.serializer_class(
                #     instance=data, context=self.get_serializer_context())

                response = Response(data, HTTP_200_OK)

                if CACV_KEY['USE_JWT']:
                    set_jwt_cookies(response, access_token, refresh_token)

                return response

            response = {
                'error': 'ERROR',
                'msg': 'Usuario o Contraseña Incorrectos'
            }
            return Response(response, HTTP_400_BAD_REQUEST)

        response = {
            'error': 'ERROR',
            'msg': 'Usuario o Contraseña Incorrectos'
        }
        return Response(response, HTTP_400_BAD_REQUEST)


# class LogoutViewSet(APIView):

#     def post(self, request, *args, **kwargs):
#         print(request.data.get('user', ''))
#         queryres = UserEmployeeModel.objects.filter(
#             id=request.data.get('user', ''))
#         if queryres.exists():
#             RefreshToken.for_user(queryres.first())
#             data = {'msg': 'OK'}
#             return Response(data, HTTP_200_OK)
#         data = {'error': 'ERROR'}
#         return Response(data, HTTP_400_BAD_REQUEST)

# class LoginViewSet(GenericViewSet):

#     permission_classes = [AllowAny]
#     serializer_class = CustomJwtTokenSerializer

#     @sensitive_post_parameters_m
#     def create(self, request):

#         username = request.data.get(
#             'user_employee_user_name', None)
#         password = request.data.get('password', None)
#         user = authenticate(username=username, password=password)

#         if user:
#             login_serializer = self.serializer_class(data=request.data)
#             if login_serializer.is_valid():
#                 user_serializer = LoginSerializer(user).data
#                 access = login_serializer.validated_data['access']
#                 refresh = login_serializer.validated_data['refresh']
#                 data = {'msg': 'OK', 'access': access,
#                         'refresh': refresh, 'user': user_serializer}
#                 return Response(data, HTTP_200_OK)
#             data = {'error': 'ERROR'}
#             return Response(data, HTTP_400_BAD_REQUEST)
#         data = {'error': 'ERROR'}
#         return Response(data, HTTP_400_BAD_REQUEST)
