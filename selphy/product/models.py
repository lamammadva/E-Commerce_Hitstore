from django.db import models
from django.urls import reverse
from colorfield.fields import ColorField



from selphy.utils.base import BaseModel
# Create your models here.
class Category(BaseModel):
    name=models.CharField(max_length=100,verbose_name='Name of the category')
    class Meta:
        verbose_name='Category'
        verbose_name_plural='All Category'
    def __str__(self):
        return self.name
class Image(BaseModel):
    image=models.ImageField(upload_to='product_image')
    class Meta:
        verbose_name = 'Image'  
        verbose_name_plural = 'Images' 
    def __str__(self):
        return f'{self.id}'
    
class Color(BaseModel):
    code=ColorField(verbose_name='Code of the color')  
    name=models.CharField(max_length=100,verbose_name='Name of the color')
    class Meta:
        verbose_name='Color'
        verbose_name_plural='All Color'
    def __str__(self):  
        return f'{self.name} color'
    
class Manufacturer(BaseModel):
    name=models.CharField(max_length=100,verbose_name='Name of the manufacturer')
    class Meta:
        verbose_name='Product Manufacturer'
        verbose_name_plural='Product Manufacturers'
    def __str__(self):
        return self.name

    
class Product(BaseModel):
    old_price=models.PositiveIntegerField(null=True,blank=True, verbose_name='old_price',)
    price=models.PositiveIntegerField()
    sale=models.BooleanField(default=True)
    title=models.CharField(max_length=100,verbose_name='Title of the product',help_text='Max 1000 character')
    category=models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category of the Product')
    manufacturer=models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Manufacturer of the Product')
    description=models.TextField(verbose_name='Description of the product')
    class Meta:
        verbose_name='Product'
        verbose_name_plural='All Products'

    @property
    def get_version(self):
        for version in self.product_version.all():
            return  version.pk
   
    def __str__(self):
        return self.title   

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={"pk": self.get_version})

class Product_version(BaseModel):
    color=models.ForeignKey(Color,on_delete=models.CASCADE,verbose_name='Color of the product',related_name='product_version_color')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_version')
    image=models.ManyToManyField(Image,related_name='product_version_image')
    cover_image=models.ImageField(upload_to='product_image',)
    
    class Meta:
        verbose_name='Product Version'
        verbose_name_plural='Product Versions'

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={"pk": self.pk})

class Review(BaseModel):
    RATING_CHOICES = [
    (1, '1 star'),
    (2, '2 stars'),
    (3, '3 stars'),
    (4, '4 stars'),
    (5, '5 stars'),
]
    quality_rating = models.PositiveIntegerField(choices=RATING_CHOICES)  # Kalite derecesi
    price_rating = models.PositiveIntegerField(choices=RATING_CHOICES)  # Fiyat derecesi
    value_rating = models.PositiveIntegerField(choices=RATING_CHOICES)  # Değer derecesi

    nickname=models.CharField(max_length=100,verbose_name='Nickname')   
    comment=models.TextField(verbose_name='Review')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='review')
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "Product Review"
        verbose_name_plural='Product Reviews'