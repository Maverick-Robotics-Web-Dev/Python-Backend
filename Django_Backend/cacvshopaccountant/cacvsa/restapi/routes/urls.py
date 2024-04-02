from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from rest_framework.routers import DefaultRouter

from restapi.employees.views import EmployeeViewSet
from restapi.owners.views import OwnCheckViewSet

from restapi.auth.views import (
    LoginViewSet,
    LogoutViewSet,
    PasswordChangeViewSet
)
from restapi.business.views import (
    WayToPayViewSet,
    VoucherTypeViewSet,
    CreditNoteViewSet,
    CreditNoteDetailViewSet,
    SaleViewSet,
    SaleDetailViewSet
)
from restapi.cashregisters.views import (
    CashRegisterViewSet,
    CashRegisterOpeningViewSet,
    CashRegisterMovementsViewSet,
    CashRegisterClosingViewSet
)
from restapi.clients.views import (
    ClientViewSet,
    ClientCheckViewSet
)
from restapi.products.views import (
    CategoryViewSet,
    BrandViewSet,
    ProductViewSet
)
from restapi.suppliers.views import (
    SupplierViewSet,
    IncomeViewSet,
    IncomeDetailViewSet
)
from restapi.users.views import (
    UserLevelViewSet,
    UserEmployeeViewSet,
    UserClientViewSet
)

router: DefaultRouter = None
urlpatterns: list = None

router = DefaultRouter()

router.register('auth/login', LoginViewSet, 'login')
router.register('auth/logout', LogoutViewSet, 'logout')
router.register('auth/passwordchange', PasswordChangeViewSet, 'passwordchange')
router.register('business/waytopay', WayToPayViewSet, 'waytopay')
router.register('business/vouchertype', VoucherTypeViewSet, 'vouchertype')
router.register('business/creditnote', CreditNoteViewSet, 'creditnote')
router.register('business/creditotedetail', CreditNoteDetailViewSet, 'creditotedetail')
router.register('business/sale', SaleViewSet, 'sale')
router.register('business/saledetail', SaleDetailViewSet, 'saledetail')
router.register('cashregisters/cashregister', CashRegisterViewSet, 'cashregister')
router.register('cashregisters/cashregisteropening', CashRegisterOpeningViewSet, 'cashregisteropening')
router.register('cashregisters/cashregistermovements', CashRegisterMovementsViewSet, 'cashregistermovements')
router.register('cashregisters/cashregisterclosing', CashRegisterClosingViewSet, 'cashregisterclosing')
router.register('clients/client', ClientViewSet, 'client')
router.register('clients/clientcheck', ClientCheckViewSet, 'clientcheck')
router.register('employees/employee', EmployeeViewSet, 'employee')
router.register('owners/owncheck', OwnCheckViewSet, 'owncheck')
router.register('products/category', CategoryViewSet, 'category')
router.register('products/brand', BrandViewSet, 'brand')
router.register('products/product', ProductViewSet, 'product')
router.register('supliers/supplier', SupplierViewSet, 'supplier')
router.register('supliers/income', IncomeViewSet, 'income')
router.register('supliers/incomedetail', IncomeDetailViewSet, 'incomedetail')
router.register('users/userlevel', UserLevelViewSet, 'userlevel')
router.register('users/useremployee', UserEmployeeViewSet, 'useremployee')
router.register('users/userclient', UserClientViewSet, 'userclient')

urlpatterns = router.urls

urlpatterns += [
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
