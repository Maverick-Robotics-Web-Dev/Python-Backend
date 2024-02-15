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
router.register('business/waytopay', WayToPayViewSet, 'waytopay')
router.register('business/vouchertype', VoucherTypeViewSet, 'vouchertype')
router.register('business/creditnote', CreditNoteViewSet, 'creditnote')
router.register('business/creditotedetail',
                CreditNoteDetailViewSet, 'creditotedetail')
router.register('business/sale', SaleViewSet, 'sale')
router.register('business/saledetail', SaleDetailViewSet, 'saledetail')
router.register('cashregisters/cashregister',
                CashRegisterViewSet, 'cashregister')
router.register('cashregisters/cashregisteropening',
                CashRegisterOpeningViewSet, 'cashregisteropening')
router.register('cashregisters/cashregistermovements',
                CashRegisterMovementsViewSet, 'cashregistermovements')
router.register('cashregisters/cashregisterclosing',
                CashRegisterClosingViewSet, 'cashregisterclosing')
router.register('clients/client', ClientViewSet, 'client')
router.register('clients/clientcheck', ClientCheckViewSet, 'clientcheck')
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
