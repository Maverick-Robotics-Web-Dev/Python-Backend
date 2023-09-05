from rest_framework import routers
from .api import UserAdminViewSet

router = routers.DefaultRouter()
router.register('api/user_admin', UserAdminViewSet, 'useradmin')

urlpatterns = router.urls
