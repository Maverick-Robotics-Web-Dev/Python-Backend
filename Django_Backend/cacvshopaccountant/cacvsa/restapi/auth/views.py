from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

# from django.conf import settings
from cacvsa.settings.base import *
from support.methods import *
from .serializers import *


class LoginViewSet(GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = CACV_KEY.LOGIN_SERIALIZER

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

        if CACV_KEY.USE_JWT:
            if CACV_KEY.JWT_AUTH_RETURN_EXPIRATION:
                response_serializer = CACV_KEY.JWT_SERIALIZER_WITH_EXPIRATION
            else:
                response_serializer = CACV_KEY.JWT_SERIALIZER
        else:
            response_serializer = CACV_KEY.TOKEN_SERIALIZER
        return response_serializer

    def login(self):
        self.user = self.serializer.validated_data['user']
        token_model = get_token_model()

        if CACV_KEY.USE_JWT:
            self.access_token, self.refresh_token = jwt_encode(self.user)
        elif token_model:
            self.token = CACV_KEY.TOKEN_CREATOR(
                token_model, self.user, self.serializer)

        if CACV_KEY.SESSION_LOGIN:
            self.process_login()


# class LoginViewSet(TokenObtainPairView):

#     serializer_class = CustomJwtTokenSerializer

#     def post(self, request):

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
