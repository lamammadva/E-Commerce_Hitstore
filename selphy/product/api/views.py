from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Product_version
from .serializers import ProductSerializers, ProductversionSerializers
from django_filters.rest_framework import DjangoFilterBackend


class CategoryAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'manufacturer']


class ColorAPIView(ListAPIView):
    queryset = Product_version.objects.all()
    serializer_class = ProductversionSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['color']


class ProductAPIView(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            obj = Product.objects.get(pk=kwargs.get('pk'))
            serializer = self.serializer_class(obj)
        else:
            all_products = Product.objects.all()
            serializer = self.serializer_class(all_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductVersionAPIView(APIView):
    queryset = Product_version.objects.all()
    serializer_class = ProductversionSerializers

    def get(self, request, *args, **kwargs):
        if kwargs.get('product_id'):
            obj = Product_version.objects.filter(
                product_id=kwargs.get('product_id'))
            stat = status.HTTP_200_OK
            result = self.serializer_class(obj, many=True).data
            if kwargs.get('pk'):
                obj = Product_version.objects.get(pk=kwargs.get('pk'))
                result = self.serializer_class(obj).data
        else:
            stat = status.HTTP_404_NOT_FOUND
            result = {'error'}
        return Response(result, status=stat)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['color']
