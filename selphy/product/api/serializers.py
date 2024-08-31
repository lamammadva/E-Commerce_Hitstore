from rest_framework import serializers
from product.models import Product,Product_version,Manufacturer,Category,Image,Color
from django.urls import reverse

class ColorVersionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Color
        fields=[
            'id',
            'name',
        ]


class CategoryVersionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=[
            'id',
            'name',
        ]
class ManufacturerVersionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Manufacturer
        fields=[
            'id',
            'name',
        ]

class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields =[
            'id',
            'image',
        ]


class ProductReadSerializers(serializers.ModelSerializer):
    category=CategoryVersionSerializers()
    manufacturer=ManufacturerVersionSerializers()
    detail_url=serializers.SerializerMethodField()
    
    class Meta:
        model=Product
        fields= [
            'id',
            'title',
            'old_price',
            'price',
            'category',
            'sale',
            'manufacturer',
            'detail_url', 
            
        ]
    
    def get_detail_url(self,obj):
        return obj.get_absolute_url()
   
class ProductversionSerializers(serializers.ModelSerializer):
    image=ImageSerializers(many=True)
    product = ProductReadSerializers()
    color = ColorVersionSerializers()
    detail_url=serializers.SerializerMethodField()

    class Meta:
        model=Product_version
        fields=[
            'id',
            'product',
            'cover_image',
            'color',
            'image',
            'detail_url',
        ]

    def get_detail_url(self,obj):
        return obj.get_absolute_url()

class ProductSerializers(serializers.ModelSerializer):
    product_version=ProductversionSerializers(many=True)
    category=CategoryVersionSerializers()
    manufacturer=ManufacturerVersionSerializers()
    detail_url=serializers.SerializerMethodField()
    class Meta:
        model=Product
        fields= [
            'id',
            'title',
            'old_price',
            'price',
            'category',
            'sale',
            'manufacturer',
            'product_version',
            'detail_url',  
            
        ]
    
 
    
    
    def get_detail_url(self,obj):
        return obj.get_absolute_url()