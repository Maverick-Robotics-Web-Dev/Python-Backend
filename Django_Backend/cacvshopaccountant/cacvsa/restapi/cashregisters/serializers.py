from rest_framework.serializers import (
    ModelSerializer,
    StringRelatedField
)

from .models import (
    CashRegisterModel,
    CashRegisterOpeningModel,
    CashRegisterMovementsModel,
    CashRegisterClosingModel
)


class CashRegisterSerializer(ModelSerializer):

    class Meta:

        model: CashRegisterModel = None
        fields: str | list = None

        model = CashRegisterModel
        fields = '__all__'


class CashRegisterRelatedSerializer(ModelSerializer):

    fk_user_employee: StringRelatedField = None

    fk_user_employee = StringRelatedField()

    class Meta:

        model: CashRegisterModel = None
        fields: str | list = None

        model = CashRegisterModel
        fields = '__all__'


class CashRegisterOpeningSerializer(ModelSerializer):

    class Meta:

        model: CashRegisterOpeningModel = None
        fields: str | list = None

        model = CashRegisterOpeningModel
        fields = '__all__'


class CashRegisterOpeningRelatedSerializer(ModelSerializer):

    fk_cash_register: StringRelatedField = None
    fk_user_employee: StringRelatedField = None

    fk_cash_register = StringRelatedField()
    fk_user_employee = StringRelatedField()

    class Meta:

        model: CashRegisterOpeningModel = None
        fields: str | list = None

        model = CashRegisterOpeningModel
        fields = '__all__'


class CashRegisterMovementsSerializer(ModelSerializer):

    class Meta:

        model: CashRegisterMovementsModel = None
        fields: str | list = None

        model = CashRegisterMovementsModel
        fields = '__all__'


class CashRegisterMovementsRelatedSerializer(ModelSerializer):

    fk_cash_register: StringRelatedField = None
    fk_way_to_pay: StringRelatedField = None
    fk_user_employee: StringRelatedField = None

    fk_cash_register = StringRelatedField()
    fk_way_to_pay = StringRelatedField()
    fk_user_employee = StringRelatedField()

    class Meta:

        model: CashRegisterMovementsModel = None
        fields: str | list = None

        model = CashRegisterMovementsModel
        fields = '__all__'


class CashRegisterClosingSerializer(ModelSerializer):

    class Meta:

        model: CashRegisterClosingModel = None
        fields: str | list = None

        model = CashRegisterClosingModel
        fields = '__all__'


class CashRegisterClosingRelatedSerializer(ModelSerializer):

    fk_cash_register: StringRelatedField = None
    fk_user_employee: StringRelatedField = None

    fk_cash_register = StringRelatedField()
    fk_user_employee = StringRelatedField()

    class Meta:

        model: CashRegisterClosingModel = None
        fields: str | list = None

        model = CashRegisterClosingModel
        fields = '__all__'
