from rest_framework.serializers import (
    ModelSerializer,
    StringRelatedField
)

from .models import OwnCheckModel


class OwnCheckSerializer(ModelSerializer):

    class Meta:

        model: OwnCheckModel = None
        fields: str = None

        model = OwnCheckModel
        fields = '__all__'


class OwnCheckRelatedSerializer(ModelSerializer):

    fk_user_employee: StringRelatedField = None

    fk_user_employee = StringRelatedField()

    class Meta:

        model: OwnCheckModel = None
        fields: str = None

        model = OwnCheckModel
        fields = '__all__'
