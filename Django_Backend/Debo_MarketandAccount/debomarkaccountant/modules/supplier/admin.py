from django.contrib import admin

from .models import *

admin.site.register([Supplier, Income, IncomeDetail])
