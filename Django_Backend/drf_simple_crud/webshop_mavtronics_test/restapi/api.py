from rest_framework import viewsets, permissions
from .models import UserAdmin
from .serializers import UserAdminSerializer


class UserAdminViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserAdmin.objects.all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = UserAdminSerializer
