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


class UserSudoSerializer(ModelSerializer):

    class Meta:

        model: UserEmployeeModel = None
        fields: str = None

        model = UserEmployeeModel
        fields = '__all__'


class UserSudoRelatedSerializer(ModelSerializer):

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
        fields: str = None

        model = UserEmployeeModel
        fields = '__all__'


class UserEmployeeRelatedSerializer(ModelSerializer):

    class Meta:

        model: UserEmployeeModel = None
        # fields: list = None
        exclude: list = None

        model = UserEmployeeModel
        # fields = ['user_name', 'password', 'login']
        exclude = ['fk_employee', 'fk_user_level', 'is_superuser', 'is_staff', 'is_active', 'groups',
                   'user_permissions', 'last_login', 'status', 'status_description', 'create_at', 'update_at']


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
