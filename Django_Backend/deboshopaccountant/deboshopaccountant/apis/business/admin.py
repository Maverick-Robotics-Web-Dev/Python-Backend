from django.contrib import admin

from .models import *

admin.site.register([WayToPayModel, VoucherTypeModel, CreditNoteModel,
                    CreditNoteDetailModel, SaleModel, SaleDetailModel])
