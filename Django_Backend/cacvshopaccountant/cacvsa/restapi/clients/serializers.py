from rest_framework.serializers import (
    ModelSerializer,
    StringRelatedField
)

from .models import (
    ClientModel,
    ClientCheckModel
)


class ClientSerializer(ModelSerializer):

    class Meta:

        model: ClientModel = None
        fields: str = None

        model = ClientModel
        fields = '__all__'


class ClientRelatedSerializer(ModelSerializer):

    fk_user_employee: StringRelatedField = None

    fk_user_employee = StringRelatedField()

    class Meta:

        model: ClientModel = None
        fields: str = None

        model = ClientModel
        fields = '__all__'


class ClientCheckSerializer(ModelSerializer):

    class Meta:

        model: ClientCheckModel = None
        fields: str = None

        model = ClientCheckModel
        fields = '__all__'


class ClientCheckRelatedSerializer(ModelSerializer):

    fk_client: StringRelatedField = None
    fk_user_employee: StringRelatedField = None

    fk_client = StringRelatedField()
    fk_user_employee = StringRelatedField()

    class Meta:

        model: ClientCheckModel = None
        fields: str = None

        model = ClientCheckModel
        fields = '__all__'
