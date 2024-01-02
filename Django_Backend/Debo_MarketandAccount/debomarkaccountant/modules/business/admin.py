from django.contrib import admin
from .models import *

admin.site.register([CreditNote , CreditNoteDetail, Sale , SaleDetail , WayToPay])
