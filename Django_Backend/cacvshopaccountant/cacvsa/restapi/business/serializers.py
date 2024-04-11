from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    StringRelatedField
)

from .models import (
    WayToPayModel,
    VoucherTypeModel,
    CreditNoteModel,
    CreditNoteDetailModel,
    SaleModel,
    SaleDetailModel
)


class WayToPaySerializer(ModelSerializer):

    class Meta:

        model: WayToPayModel = None
        fields: str | list = None

        model = WayToPayModel
        fields = '__all__'


class WayToPayRelatedSerializer(ModelSerializer):

    fk_user_employee: StringRelatedField = None

    fk_user_employee = StringRelatedField()

    class Meta:

        model: WayToPayModel = None
        fields: str | list = None

        model = WayToPayModel
        fields = '__all__'


class VoucherTypeSerializer(ModelSerializer):

    class Meta:

        model: VoucherTypeModel = None
        fields: str | list = None

        model = VoucherTypeModel
        fields = '__all__'


class VoucherTypeRelatedSerializer(ModelSerializer):

    fk_user_employee: StringRelatedField = None

    fk_user_employee = StringRelatedField()

    class Meta:

        model: VoucherTypeModel = None
        fields: str | list = None

        model = VoucherTypeModel
        fields = '__all__'


class CreditNoteDetailAllSerializer(ModelSerializer):

    class Meta:

        model: CreditNoteDetailModel = None
        fields: str | list = None

        model = CreditNoteDetailModel
        fields = '__all__'


class CreditNoteDetailSerializer(ModelSerializer):

    class Meta:

        model: CreditNoteDetailModel = None
        fields: str | list = None
        exclude: list = None

        model = CreditNoteDetailModel
        fields = '__all__'
        read_only_fields = ['fk_credit_note']


class CreditNoteDetailRelatedSerializer(ModelSerializer):

    fk_credit_note: StringRelatedField = None
    fk_product: StringRelatedField = None

    fk_credit_note = StringRelatedField()
    fk_product = StringRelatedField()

    class Meta:

        model: CreditNoteDetailModel = None
        fields: str | list = None

        model = CreditNoteDetailModel
        fields = '__all__'


# class CreditNoteSerializer(ModelSerializer):

#     class Meta:

#         model: CreditNoteModel = None
#         fields: str | list = None

#         model = CreditNoteModel
#         fields = '__all__'


class CreditNoteSerializer(ModelSerializer):

    detail: Serializer = None

    detail = CreditNoteDetailSerializer(many=True)

    class Meta:

        model: CreditNoteModel = None
        fields: str | list = None

        model = CreditNoteModel
        fields = '__all__'


class CreditNoteRelatedSerializer(ModelSerializer):

    fk_client: StringRelatedField = None
    fk_user_employee: StringRelatedField = None
    detail: Serializer = None

    fk_client = StringRelatedField()
    fk_user_employee = StringRelatedField()
    detail = CreditNoteDetailRelatedSerializer(many=True, source='note_detail')

    class Meta:

        model: CreditNoteModel = None
        fields: str | list = None

        model = CreditNoteModel
        fields = '__all__'


class SaleDetailSerializer(ModelSerializer):

    class Meta:

        model: SaleDetailModel = None
        fields: str | list = None

        model = SaleDetailModel
        fields = '__all__'


class SaleDetailRelatedSerializer(ModelSerializer):

    fk_sale: StringRelatedField = None
    fk_product: StringRelatedField = None

    fk_sale = StringRelatedField()
    fk_product = StringRelatedField()

    class Meta:

        model: SaleDetailModel = None
        fields: str | list = None

        model = SaleDetailModel
        fields = '__all__'


class SaleSerializer(ModelSerializer):

    class Meta:

        model: SaleModel = None
        fields: str | list = None

        model = SaleModel
        fields = '__all__'


class SaleRelatedSerializer(ModelSerializer):

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
        fields: str | list = None

        model = SaleModel
        fields = '__all__'
