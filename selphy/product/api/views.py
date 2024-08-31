from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Product_version
from .serializers import ProductSerializers, ProductversionSerializers
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ProductApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_version__color','category','manufacturer']
   
    def get(self, request, *args, **kwargs):
        color_id = request.GET.get('product_version__color')
        if color_id:
            version= Product_version.objects.filter(color__id=color_id)
            serializer = ProductversionSerializers(version,many=True)
            return Response(serializer.data)
        if kwargs.get('pk'):
            try:
                product = Product.objects.get(pk=kwargs.get('pk'))
            except Product.DoesNotExist:
                return Response({"not found with id"},status=status.HTTP_404_NOT_FOUND)
            color_id = request.GET.get('product_version__color')
            if color_id:
                version = product.product_version.filter(color__id = color_id).first()
                if not version:
                    return Response({"not foound version with color"},status=status.HTTP_404_NOT_FOUND)
                serializer = ProductversionSerializers(version)
            elif kwargs.get('version_pk'):
                try:
                     version = product.product_version.get(pk=kwargs.get('version_pk'))
                except Product_version.DoesNotExist:
                    return Response({"not found product with version"},status=status.HTTP_404_NOT_NOT)
                serializer = ProductversionSerializers(version)
            else:
                serializer = self.serializer_class(product)
            return Response(serializer.data)
        filtered_products = self.filter_queryset(self.get_queryset())
        serializer = self.serializer_class(filtered_products, many=True)
        return Response(serializer.data)

        





  



