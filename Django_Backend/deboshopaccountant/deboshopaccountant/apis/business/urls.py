from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('waytopay', WayToPayViewSet, 'waytopay')
router.register('vouchertype', VoucherTypeViewSet, 'waytopay')
urlpatterns = router.urls
