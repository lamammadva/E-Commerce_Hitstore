from django.contrib import admin
from .models import Blogs,Comments,Author,Category
from modeltranslation.admin import TranslationAdmin
from django.utils.html import format_html
# Create ckeditor for flatpages
# from django.contrib.flatpages.models import FlatPage
# from .forms import Flatpageform
# from django.utils.translation import gettext_lazy as _



admin.site.site_header = "Hitstore admin panel"
admin.site.site_title = 'Hitstore'

class BlogAdmin(TranslationAdmin):
    list_display = ('title','description','author','get_media','created_at','updated_at','category')
    list_filter = ['is_advice','category']
    list_editable = ['author']
    search_fields = ['title']
     



    def get_media(self,obj):
        if obj.category.name == 'Image' :
            return format_html('<img src="{url}" width="190px" height="100px" type="image/jpg" target="_blank"></a>'.format(url=obj.file.url))

        elif obj.category.name== 'Video' :
            return format_html('<video controls width="100px"><source src="{url}"  type="video/mp4" target="_blank">View Video </a> '.format(url=obj.file.url))

        elif obj.category.name== 'Audio':
            return format_html('<audio controls><source src="{url}" type="audio/mp3" target="_blank">Listen Audio </a>'.format(url=obj.file.url))

class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','comment')

class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)  




admin.site.register(Author)
admin.site.register(Blogs,BlogAdmin)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Comments,CommentAdmin)
# reate ckeditor for flatpages
# admin.site.unregister(FlatPage)
# @admin.register(FlatPage)
# class FlatPageAdmin(admin.ModelAdmin):
#     form=Flatpageform
    

   



# class BlogAddVersion(admin.TabularInline):
#     model=Blogs
#     extra=1

# class AuthorAdmin(admin.ModelAdmin):
#     inlines= [BlogAddVersion]
    




