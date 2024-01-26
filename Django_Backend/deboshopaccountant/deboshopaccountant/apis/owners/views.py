from rest_framework import viewsets, permissions

from .models import *
from .serializers import *


class OwnCheckViewSet(viewsets.ModelViewSet):
    queryset = OwnCheckModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OwnCheckSerializer
