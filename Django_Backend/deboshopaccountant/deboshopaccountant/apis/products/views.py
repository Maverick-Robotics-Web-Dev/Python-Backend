from rest_framework import viewsets, permissions

from .models import *
from .serializers import *


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = BrandModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BrandSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer
