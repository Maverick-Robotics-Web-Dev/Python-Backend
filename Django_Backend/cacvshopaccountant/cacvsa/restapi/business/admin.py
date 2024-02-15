from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register([WayToPayModel, VoucherTypeModel, CreditNoteModel,
                    CreditNoteDetailModel, SaleModel, SaleDetailModel])
