from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apis.business.views import *
from apis.cashregisters.views import *
from apis.clients.views import *
from apis.employees.views import *
from apis.owners.views import *
from apis.products.views import *
from apis.suppliers.views import *
from apis.users.views import *


router = routers.DefaultRouter()
router.register('waytopay', WayToPayViewSet, 'waytopay')
router.register('vouchertype', VoucherTypeViewSet, 'vouchertype')
router.register('creditnote', CreditNoteViewSet, 'creditnote')
router.register('creditotedetail', CreditNoteDetailViewSet, 'creditotedetail')
router.register('sale', SaleViewSet, 'sale')
router.register('saledetail', SaleDetailViewSet, 'saledetail')
router.register('cashregister', CashRegisterViewSet, 'cashregister')
router.register('cashregisteropening',
                CashRegisterOpeningViewSet, 'cashregisteropening')
router.register('cashregistermovements',
                CashRegisterMovementsViewSet, 'cashregistermovements')
router.register('cashregisterclosing',
                CashRegisterClosingViewSet, 'cashregisterclosing')
router.register('client', ClientViewSet, 'client')
router.register('clientcheck', ClientCheckViewSet, 'clientcheck')
router.register('employee', EmployeeViewSet, 'employee')
router.register('owncheck', OwnCheckViewSet, 'owncheck')
router.register('category', CategoryViewSet, 'category')
router.register('brand', BrandViewSet, 'brand')
router.register('product', ProductViewSet, 'product')
router.register('supplier', SupplierViewSet, 'supplier')
router.register('income', IncomeViewSet, 'income')
router.register('incomedetail', IncomeDetailViewSet, 'incomedetail')
router.register('userlevel', UserLevelViewSet, 'userlevel')
router.register('useremployee', UserEmployeeViewSet, 'useremployee')
router.register('userclient', UserClientViewSet, 'userclient')
urlpatterns = router.urls
