from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.status import *

from .models import *
from .serializers import *


class CategoryViewSet(GenericViewSet):

    model = CategoryModel
    serializer_class = CategorySerializer

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            return self.model.objects.filter(category_status=True)
        return self.queryset

    def list(self, request):
        # print(request)
        queryres = self.get_queryset()
        serializer = self.serializer_class(queryres, many=True)
        data = {'msg': 'OK', 'data': serializer.data}
        return Response(data, HTTP_200_OK)

    def retrieve(self, request, pk=None):
        # print(pk)
        queryres = self.get_object(pk)
        serializer = self.serializer_class(queryres)
        data = {'msg': 'OK', 'data': serializer.data}
        return Response(data, HTTP_200_OK)

    def create(self, request):
        # print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'msg': 'OK', 'data': serializer.data}
            return Response(data, HTTP_201_CREATED)
        data = {'msg': 'ERROR', 'errors': serializer.errors}
        return Response(data, HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryres = self.get_object(pk)
        serializer = self.serializer_class(
            queryres, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {'msg': 'OK', 'data': serializer.data}
            return Response(data, HTTP_201_CREATED)
        data = {'msg': 'ERROR', 'errors': serializer.errors}
        return Response(data, HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryres = self.model.objects.filter(
            category_id=pk).update(category_status=False)
        if queryres == 1:
            data = {'msg': 'OK'}
            return Response(data, HTTP_200_OK)
        data = {'msg': 'ERROR'}
        return Response(data, HTTP_404_NOT_FOUND)


class BrandViewSet(GenericViewSet):

    model = BrandModel
    serializer_class = BrandSerializer

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            return self.model.objects.filter(brand_status=True)
        return self.queryset

    def list(self, request):
        # print(request)
        queryres = self.get_queryset()
        serializer = self.serializer_class(queryres, many=True)
        data = {'msg': 'OK', 'data': serializer.data}
        return Response(data, HTTP_200_OK)

    def retrieve(self, request, pk=None):
        # print(pk)
        queryres = self.get_object(pk)
        serializer = self.serializer_class(queryres)
        data = {'msg': 'OK', 'data': serializer.data}
        return Response(data, HTTP_200_OK)

    def create(self, request):
        # print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'msg': 'OK', 'data': serializer.data}
            return Response(data, HTTP_201_CREATED)
        data = {'msg': 'ERROR', 'errors': serializer.errors}
        return Response(data, HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryres = self.get_object(pk)
        serializer = self.serializer_class(
            queryres, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {'msg': 'OK', 'data': serializer.data}
            return Response(data, HTTP_201_CREATED)
        data = {'msg': 'ERROR', 'errors': serializer.errors}
        return Response(data, HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryres = self.model.objects.filter(
            brand_id=pk).update(brand_status=False)
        if queryres == 1:
            data = {'msg': 'OK'}
            return Response(data, HTTP_200_OK)
        data = {'msg': 'ERROR'}
        return Response(data, HTTP_404_NOT_FOUND)


class ProductViewSet(GenericViewSet):

    model = ProductModel
    serializer_class = ProductSerializer

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            return self.model.objects.filter(product_status=True)
        return self.queryset

    def list(self, request):
        # print(request)
        queryres = self.get_queryset()
        serializer = self.serializer_class(queryres, many=True)
        data = {'msg': 'OK', 'data': serializer.data}
        return Response(data, HTTP_200_OK)

    def retrieve(self, request, pk=None):
        # print(pk)
        queryres = self.get_object(pk)
        serializer = self.serializer_class(queryres)
        data = {'msg': 'OK', 'data': serializer.data}
        return Response(data, HTTP_200_OK)

    def create(self, request):
        # print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'msg': 'OK', 'data': serializer.data}
            return Response(data, HTTP_201_CREATED)
        data = {'msg': 'ERROR', 'errors': serializer.errors}
        return Response(data, HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryres = self.get_object(pk)
        serializer = self.serializer_class(
            queryres, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {'msg': 'OK', 'data': serializer.data}
            return Response(data, HTTP_201_CREATED)
        data = {'msg': 'ERROR', 'errors': serializer.errors}
        return Response(data, HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryres = self.model.objects.filter(
            product_id=pk).update(product_status=False)
        if queryres == 1:
            data = {'msg': 'OK'}
            return Response(data, HTTP_200_OK)
        data = {'msg': 'ERROR'}
        return Response(data, HTTP_404_NOT_FOUND)
