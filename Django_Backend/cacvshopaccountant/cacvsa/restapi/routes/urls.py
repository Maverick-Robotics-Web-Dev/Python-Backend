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
    UserSudoViewSet,
    UserEmployeeViewSet,
    UserClientViewSet
)

router: DefaultRouter = None
urlpatterns: list = None

router = DefaultRouter()

router.register('auth/login', LoginViewSet, 'login')
router.register('auth/logout', LogoutViewSet, 'logout')
router.register('auth/password-change', PasswordChangeViewSet, 'password-change')
router.register('business/way-to-pay', WayToPayViewSet, 'way-to-pay')
router.register('business/voucher-type', VoucherTypeViewSet, 'voucher-type')
router.register('business/credit-note', CreditNoteViewSet, 'credit-note')
router.register('business/credit-note-detail', CreditNoteDetailViewSet, 'credit-note-detail')
router.register('business/sale', SaleViewSet, 'sale')
router.register('business/sale-detail', SaleDetailViewSet, 'sale-detail')
router.register('cashregisters/cash-register', CashRegisterViewSet, 'cash-register')
router.register('cashregisters/cash-register-opening', CashRegisterOpeningViewSet, 'cash-register-opening')
router.register('cashregisters/cash-register-movements', CashRegisterMovementsViewSet, 'cash-register-movements')
router.register('cashregisters/cash-register-closing', CashRegisterClosingViewSet, 'cash-register-closing')
router.register('clients/client', ClientViewSet, 'client')
router.register('clients/client-check', ClientCheckViewSet, 'client-check')
router.register('employees/employee', EmployeeViewSet, 'employee')
router.register('owners/own-check', OwnCheckViewSet, 'own-check')
router.register('products/category', CategoryViewSet, 'category')
router.register('products/brand', BrandViewSet, 'brand')
router.register('products/product', ProductViewSet, 'product')
router.register('supliers/supplier', SupplierViewSet, 'supplier')
router.register('supliers/income', IncomeViewSet, 'income')
router.register('supliers/income-detail', IncomeDetailViewSet, 'income-detail')
router.register('users/user-level', UserLevelViewSet, 'user-level')
router.register('users/user-sudo', UserSudoViewSet, 'user-sudo')
router.register('users/user-employee', UserEmployeeViewSet, 'user-employee')
router.register('users/user-client', UserClientViewSet, 'user-client')

urlpatterns = router.urls

urlpatterns += [
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
