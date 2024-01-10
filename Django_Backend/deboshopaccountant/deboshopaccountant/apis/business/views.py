from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import WayToPayModel
from .serializers import WayToPaySerializer

class WayToPayModelViewSet(viewsets.ModelViewSet):
    queryset = WayToPayModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = WayToPaySerializer
