from rest_framework.serializers import ModelSerializer, StringRelatedField

from .models import *
from restapi.users.serializers import UserEmployeeSerializer


class WayToPaySerializer(ModelSerializer):

    # Method 1
    # fk_user_employee = UserEmployeeSerializer()
    # Method 2
    fk_user_employee = StringRelatedField()

    class Meta:
        model = WayToPayModel
        fields = '__all__'
        read_only_fields = ['way_to_pay_id']


class VoucherTypeSerializer(ModelSerializer):

    fk_user_employee = StringRelatedField()

    class Meta:
        model = VoucherTypeModel
        fields = '__all__'
        read_only_fields = ['voucher_type_id']


class CreditNoteSerializaer(ModelSerializer):

    fk_client = StringRelatedField()
    fk_user_employee = StringRelatedField()

    class Meta:
        model = CreditNoteModel
        fields = '__all__'
        read_only_fields = ['credit_note_id']


class CreditNoteDetailSerializer(ModelSerializer):

    fk_credit_note = StringRelatedField()
    fk_product = StringRelatedField()
    fk_user_employee = StringRelatedField()

    class Meta:
        model = CreditNoteDetailModel
        fields = '__all__'
        read_only_fields = ['credit_note_detail_id']


class SaleSerializer(ModelSerializer):

    fk_user_employee = StringRelatedField()

    class Meta:
        model = SaleModel
        fields = '__all__'
        read_only_fields = ['sale_id']


class SaleDetailSerializer(ModelSerializer):

    fk_user_employee = StringRelatedField()

    class Meta:
        model = SaleDetailModel
        fields = '__all__'
        read_only_fields = ['sale_detail_id']
