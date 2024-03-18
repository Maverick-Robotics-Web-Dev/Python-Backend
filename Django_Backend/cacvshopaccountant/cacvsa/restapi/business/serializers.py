from rest_framework.serializers import ModelSerializer, StringRelatedField

from .models import *
from restapi.users.serializers import UserEmployeeSerializer


class WayToPaySerializer(ModelSerializer):

    class Meta:

        model: WayToPayModel = None
        fields: str | list[str] = None
        read_only_fields: list[str] = None

        model = WayToPayModel
        fields = '__all__'
        read_only_fields = ['id']


class WayToPayRelatedSerializer(ModelSerializer):

    fk_user_employee: StringRelatedField = None
    fk_user_employee = StringRelatedField()

    class Meta:

        model: WayToPayModel = None
        fields: str | list[str] = None
        read_only_fields: list[str] = None

        model = WayToPayModel
        fields = '__all__'
        read_only_fields = ['id']


class VoucherTypeSerializer(ModelSerializer):

    fk_user_employee: StringRelatedField = None

    fk_user_employee = StringRelatedField()

    class Meta:

        model: VoucherTypeModel = None
        fields: str | list[str] = None
        read_only_fields: list[str] = None

        model = VoucherTypeModel
        fields = '__all__'
        read_only_fields = ['id']


class CreditNoteSerializaer(ModelSerializer):

    fk_client: StringRelatedField = None
    fk_user_employee: StringRelatedField = None

    fk_client = StringRelatedField()
    fk_user_employee = StringRelatedField()

    class Meta:

        model: CreditNoteModel = None
        fields: str | list[str] = None
        read_only_fields: list[str] = None

        model = CreditNoteModel
        fields = '__all__'
        read_only_fields = ['id']


class CreditNoteDetailSerializer(ModelSerializer):

    fk_credit_note: StringRelatedField = None
    fk_product: StringRelatedField = None

    fk_credit_note = StringRelatedField()
    fk_product = StringRelatedField()

    class Meta:

        model: CreditNoteDetailModel = None
        fields: str | list[str] = None
        read_only_fields: list[str] = None

        model = CreditNoteDetailModel
        fields = '__all__'
        read_only_fields = ['id']


class SaleSerializer(ModelSerializer):

    fk_client: StringRelatedField = None
    fk_sale_voucher_type: StringRelatedField = None
    fk_way_to_pay: StringRelatedField = None
    fk_user_employee: StringRelatedField = None

    fk_client = StringRelatedField()
    fk_sale_voucher_type = StringRelatedField()
    fk_way_to_pay = StringRelatedField()
    fk_user_employee = StringRelatedField()

    class Meta:

        model: SaleModel = None
        fields: str | list[str] = None
        read_only_fields: list[str] = None

        model = SaleModel
        fields = '__all__'
        read_only_fields = ['id']


class SaleDetailSerializer(ModelSerializer):

    fk_sale: StringRelatedField = None
    fk_product: StringRelatedField = None

    fk_sale = StringRelatedField()
    fk_product = StringRelatedField()

    class Meta:

        model: SaleDetailModel = None
        fields: str | list[str] = None
        read_only_fields: list[str] = None

        model = SaleDetailModel
        fields = '__all__'
        read_only_fields = ['id']
