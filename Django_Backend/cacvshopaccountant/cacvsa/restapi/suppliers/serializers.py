from rest_framework.serializers import (
    ModelSerializer,
    StringRelatedField
)

from .models import (
    SupplierModel,
    IncomeModel,
    IncomeDetailModel
)


class SupplierSerializer(ModelSerializer):

    class Meta:

        model: SupplierModel = None
        fields: str = None

        model = SupplierModel
        fields = '__all__'


class SupplierRelatedSerializer(ModelSerializer):

    fk_user_employee: StringRelatedField = None

    fk_user_employee = StringRelatedField()

    class Meta:

        model: SupplierModel = None
        fields: str = None

        model = SupplierModel
        fields = '__all__'


class IncomeSerializer(ModelSerializer):

    class Meta:

        model: IncomeModel = None
        fields: str = None

        model = IncomeModel
        fields = '__all__'


class IncomeRelatedSerializer(ModelSerializer):

    fk_supplier: StringRelatedField = None
    fk_user_employee: StringRelatedField = None

    fk_supplier = StringRelatedField()
    fk_user_employee = StringRelatedField()

    class Meta:

        model: IncomeModel = None
        fields: str = None

        model = IncomeModel
        fields = '__all__'


class IncomeDetailSerializer(ModelSerializer):

    class Meta:

        model: IncomeDetailModel = None
        fields: str = None

        model = IncomeDetailModel
        fields = '__all__'


class IncomeDetailRelatedSerializer(ModelSerializer):

    fk_income: StringRelatedField = None
    fk_product: StringRelatedField = None

    fk_income = StringRelatedField()
    fk_product = StringRelatedField()

    class Meta:

        model: IncomeDetailModel = None
        fields: str = None

        model = IncomeDetailModel
        fields = '__all__'
