from rest_framework import routers

from .views import WayToPayModelViewSet

router = routers.DefaultRouter()
router.register('api/waytopay', WayToPayModelViewSet, 'waytopay')
urlpatterns = router.urls