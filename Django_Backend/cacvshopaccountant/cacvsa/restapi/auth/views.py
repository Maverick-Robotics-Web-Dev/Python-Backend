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
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    user = None
    access_token = None
    refresh_token = None
    token = None

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def process_login(self):
        django_login(self.request, self.user)

    def get_response_serializer(self):

        if CACV_KEY['USE_JWT']:
            if CACV_KEY['JWT_AUTH_RETURN_EXPIRATION']:
                response_serializer = JWTSerializerWithExpiration
            else:
                response_serializer = JWTSerializer
        else:
            response_serializer = TokenSerializer
        return response_serializer

    def login(self, user):
        print(self.serializer.validated_data)
        self.user = user
        token_model = get_token_model()

        if CACV_KEY['USE_JWT']:
            self.access_token, self.refresh_token = jwt_encode(self.user)
        elif token_model:
            self.token = default_create_token(
                token_model, self.user, self.serializer)

        if CACV_KEY['SESSION_LOGIN']:
            self.process_login()

    def get_response(self):
        serializer_class = self.get_response_serializer()

        if CACV_KEY['USE_JWT']:
            access_token_expiration = (
                timezone.now() + jwt_settings.ACCESS_TOKEN_LIFETIME)
            refresh_token_expiration = (
                timezone.now() + jwt_settings.REFRESH_TOKEN_LIFETIME)
            return_expiration_times = CACV_KEY['JWT_AUTH_RETURN_EXPIRATION']
            auth_httponly = CACV_KEY['JWT_AUTH_HTTPONLY']

            data = {
                'user': self.user,
                'access': self.access_token,
                'refresh': self.refresh_token,
                'OK': 'OK',
                'msg': 'Usuario o Contraseña Incorrectos'
            }

            if return_expiration_times:
                data['access_expiration'] = access_token_expiration
                data['refresh_expiration'] = refresh_token_expiration

            serializer = serializer_class(
                instance=data,
                context=self.get_serializer_context(),
            )
        elif self.token:
            serializer = serializer_class(
                instance=self.token,
                context=self.get_serializer_context(),
            )
        else:
            return Response(status=HTTP_204_NO_CONTENT)

        response = Response(serializer.data, status=HTTP_200_OK)
        if CACV_KEY['USE_JWT']:
            set_jwt_cookies(response, self.access_token, self.refresh_token)
        return response

    # @action(detail=False, methods=['post'], url_path='login')
    def create(self, request):

        username = request.data.get(
            'user_employee_user_name', None)
        password = request.data.get('password', None)

        user = authenticate(username=username, password=password)

        if user:
            self.serializer = self.get_serializer(data=self.request.data)
            self.serializer.is_valid(raise_exception=True)
            self.login(user)

        else:

            data = {
                'error': 'ERROR',
                'msg': 'Usuario o Contraseña Incorrectos'
            }

            return Response(data, HTTP_400_BAD_REQUEST)

        return self.get_response()

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
