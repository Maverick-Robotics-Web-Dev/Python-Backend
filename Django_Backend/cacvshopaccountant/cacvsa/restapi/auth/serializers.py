from rest_framework.serializers import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from restapi.users.models import *
from restapi.support.methods import get_token_model


class CustomJwtTokenSerializer(TokenObtainPairSerializer):
    pass


class LoginSerializer(ModelSerializer):

    class Meta:
        model = UserEmployeeModel
        fields = ['id', 'user_employee_user_name']
        read_only_fields = ['id', 'user_employee_user_name']


class JWTSerializer(Serializer):
    """
    Serializer for JWT authentication.
    """
    access = CharField()
    refresh = CharField()
    user = SerializerMethodField()

    def get_user(self, obj):
        """
        Required to allow using custom USER_DETAILS_SERIALIZER in
        JWTSerializer. Defining it here to avoid circular imports
        """
        if api_settings.LOGIN_SERIALIZER:
            JWTUserDetailsSerializer = api_settings.LOGIN_SERIALIZER
        else:
            JWTUserDetailsSerializer = LoginSerializer()

        user_data = JWTUserDetailsSerializer(
            obj['user'], context=self.context).data
        return user_data


class JWTSerializerWithExpiration(JWTSerializer):
    """
    Serializer for JWT authentication with expiration times.
    """
    access_expiration = DateTimeField()
    refresh_expiration = DateTimeField()


class TokenSerializer(ModelSerializer):
    """
    Serializer for Token model.
    """

    class Meta:
        model = get_token_model()
        fields = ('key',)
