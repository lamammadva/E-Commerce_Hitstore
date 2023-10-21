from django.contrib import admin
from product.models import *
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin
# Register your models here.
class ProductAdmin(TranslationAdmin):
    list_display=('title', 'price','sale','category')
    

    

class Product_versionAdmin(admin.ModelAdmin):
    list_display=('color','get_image',)
    def get_image(self,obj):
        if obj.cover_image:
            img = '<img src="{url}" width="250px" height="170px"/>'.format(url=obj.cover_image.url)
            return format_html(img)
    get_image.short_description ='image'

class ReviewAdmin(admin.ModelAdmin):
    list_display=('nickname','comment',) 
    readonly_fields=['created_at','updated_at']   

admin.site.register(Review,ReviewAdmin)   
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Product,ProductAdmin)
admin.site.register(Color)
admin.site.register(Product_version,Product_versionAdmin)
admin.site.register(Image)