from django.db import models
from selphy.utils.base import BaseModel
from django.core.validators import FileExtensionValidator
from ckeditor_uploader.fields import RichTextUploadingField 

# Create your models here. 
class Author(BaseModel):
    title=models.CharField(max_length=100,verbose_name='Title of the author',help_text='Max 100 characters')

    class Meta:
        verbose_name='Author'
        verbose_name_plural='All Author'
    def __str__(self):
        return self.title
class Category(BaseModel):
    Blog_type=(
        ('Image','Image'),
        ('Video','Video'),
        ('Audio','Audio'),
    )
    name=models.CharField(choices=Blog_type, max_length=100, verbose_name='Name of the category',help_text='Max 100 character')  

    class Meta:
        verbose_name='Category'
        verbose_name_plural="All Category"
    def get_type_display_name(self):
        return dict(self.Blog_type).get(self.name)
      
    def __str__(self):
        return self.name


  
class Blogs(BaseModel):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Category of the blog')
    title=models.CharField(max_length=100,verbose_name='Title of the blog',help_text='Max 100 character')
    description=models.TextField(verbose_name='Description of the blog', help_text= 'Max 1000 characters')
    author= models.ForeignKey(Author,on_delete=models.CASCADE,verbose_name='Author  of the blog',)
    is_advice = models.BooleanField(default=True,verbose_name='Is this advice blog?')
    file = models.FileField(upload_to='file',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','jpg','avi','mp3','mp4','webp','mkv','gi','jpeg','png','ogg','html','htm','wmv'])])
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural= 'All Blog'
    
    def __str__(self):
        return self.title
    
class Comments(BaseModel):  
    name=models.CharField(max_length=100, verbose_name='Name:')
    email=models.EmailField(verbose_name='Email adsress:')
    comment=models.TextField(verbose_name='Comment:')
    blog=models.ForeignKey(Blogs,on_delete=models.CASCADE,related_name='comments')

    class Meta:
        verbose_name='Comment'
        verbose_name_plural='All Comment'
    def __str__(self):
        return self.name









