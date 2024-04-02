from rest_framework.serializers import (
    ModelSerializer,
    StringRelatedField
)

from .models import (
    UserLevelModel,
    UserEmployeeModel,
    UserClientModel
)


class UserLevelSerializer(ModelSerializer):

    class Meta:

        model: UserLevelModel = None
        fields: str = None

        model = UserLevelModel
        fields = '__all__'


class UserLevelRelatedSerializer(ModelSerializer):

    fk_user_employee: StringRelatedField = None

    fk_user_employee = StringRelatedField()

    class Meta:

        model: UserLevelModel = None
        fields: str = None

        model = UserLevelModel
        fields = '__all__'


class UserAdminSerializer(ModelSerializer):

    class Meta:

        model: UserEmployeeModel = None
        exclude: list = None

        model = UserEmployeeModel
        exclude = ['groups', 'user_permissions']


class UserAdminRelatedSerializer(ModelSerializer):

    fk_employee: StringRelatedField = None
    fk_user_level: StringRelatedField = None

    fk_employee = StringRelatedField()
    fk_user_level = StringRelatedField()

    class Meta:

        model: UserEmployeeModel = None
        exclude: list = None

        model = UserEmployeeModel
        exclude = ['groups', 'user_permissions']


class UserEmployeeSerializer(ModelSerializer):

    class Meta:

        model: UserEmployeeModel = None
        fields: list = None

        model = UserEmployeeModel
        fields = ['user_name', 'password', 'login']
        # exclude = ['groups', 'user_permissions']


class UserEmployeeRelatedSerializer(ModelSerializer):

    fk_employee: StringRelatedField = None
    fk_user_level: StringRelatedField = None

    fk_employee = StringRelatedField()
    fk_user_level = StringRelatedField()

    class Meta:

        model: UserEmployeeModel = None
        fields: list = None

        model = UserEmployeeModel
        fields = ['user_name', 'password', 'login']
        # exclude = ['groups', 'user_permissions']


class UserClientSerializer(ModelSerializer):

    class Meta:

        model: UserClientModel = None
        fields: str = None

        model = UserClientModel
        fields = '__all__'


class UserClientRelatedSerializer(ModelSerializer):

    fk_client: StringRelatedField = None

    fk_client = StringRelatedField()

    class Meta:

        model: UserClientModel = None
        fields: str = None

        model = UserClientModel
        fields = '__all__'
