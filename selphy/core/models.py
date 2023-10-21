from django.db import models
from selphy.utils.base import BaseModel
# Create your models here.

class Core(BaseModel):
    description=models.TextField(verbose_name='Description of the person',help_text='Max 100 character')
    name=models.CharField(max_length=100,verbose_name='Name of the person')
    image=models.ImageField(upload_to='core_image',verbose_name='Image of the person')
    class Meta:
        verbose_name='Core'
        verbose_name_plural='All Core'
    
    def __str__(self):
        return self.name
    
class Subscriber(BaseModel):
    email=models.EmailField(verbose_name='Email Address')

    class Meta:
        verbose_name='Subscriber'
        verbose_name_plural='Subscribers'
        
    def __str__(self):
        return self.email
    
class ContactUs(BaseModel):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()

    class Meta:
        verbose_name='Contact Us'
        verbose_name_plural ='Contact Us'
    def __str__(self):
        return self.first_name