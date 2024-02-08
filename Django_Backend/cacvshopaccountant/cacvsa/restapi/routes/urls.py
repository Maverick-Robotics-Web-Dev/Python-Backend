from rest_framework.routers import DefaultRouter

from restapi.business.views import *
from restapi.cashregisters.views import *
from restapi.clients.views import *
from restapi.employees.views import *
from restapi.owners.views import *
from restapi.products.views import *
from restapi.suppliers.views import *
from restapi.users.views import *

router = DefaultRouter()
router.register('waytopay', WayToPayViewSet, basename='waytopay')
# router.register('vouchertype', VoucherTypeViewSet, 'vouchertype')
# router.register('creditnote', CreditNoteViewSet, 'creditnote')
# router.register('creditotedetail', CreditNoteDetailViewSet, 'creditotedetail')
# router.register('sale', SaleViewSet, 'sale')
# router.register('saledetail', SaleDetailViewSet, 'saledetail')
# router.register('cashregister', CashRegisterViewSet, 'cashregister')
# router.register('cashregisteropening',
#                 CashRegisterOpeningViewSet, 'cashregisteropening')
# router.register('cashregistermovements',
#                 CashRegisterMovementsViewSet, 'cashregistermovements')
# router.register('cashregisterclosing',
#                 CashRegisterClosingViewSet, 'cashregisterclosing')
# router.register('client', ClientViewSet, 'client')
# router.register('clientcheck', ClientCheckViewSet, 'clientcheck')
# router.register('employee', EmployeeViewSet, 'employee')
# router.register('owncheck', OwnCheckViewSet, 'owncheck')
# router.register('category', CategoryViewSet, 'category')
# router.register('brand', BrandViewSet, 'brand')
# router.register('product', ProductViewSet, 'product')
# router.register('supplier', SupplierViewSet, 'supplier')
# router.register('income', IncomeViewSet, 'income')
# router.register('incomedetail', IncomeDetailViewSet, 'incomedetail')
# router.register('userlevel', UserLevelViewSet, 'userlevel')
# router.register('useremployee', UserEmployeeViewSet, 'useremployee')
# router.register('userclient', UserClientViewSet, 'userclient')
urlpatterns = router.urls
