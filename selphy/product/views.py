from typing import Any, Dict, Optional
from django.db import models
from user.models import CustomUser
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.views.generic import ListView,DetailView,CreateView
from jinja2 import Environment, FileSystemLoader
from .models import *
from .forms import ReviewForm 
# Create your views her
# e.


class Productview(ListView):
    model = Product
    paginate_by = 8
    template_name = 'product.html'
    context_object_name = 'products'
    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category']=Category.objects.all()
        context['color']=Color.objects.all()
        context['manufacturer']=Manufacturer.objects.all()
        return context


class ProductdetailView(DetailView,CreateView):
    model= Product
    template_name='product_detail.html'
    context_object_name='product_detail'
    form_class=ReviewForm

    def get_object(self):
        return Product_version.objects.filter(pk=self.kwargs['pk']).first()   #hal hazirda oldugumuz versiya
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        product_color=[]
        product=Product.objects.get(product_version=self.get_object())
        product_versions=product.product_version.all()
        related_product=Product.objects.filter(category=product.category).exclude(product_version=self.get_object())

        for version in product_versions:
            product_color.append({'id': version.id, 'product': version.product.id, 'color': version.color})
        context['colors']=product_color
        context['image']=self.get_object().image.all()
        context['related']=related_product
        context['reviews']=Review.objects.order_by('-created_at')
        context['review_form']=ReviewForm()
        

        return context
        
    

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            comment= form.save(commit=False)
            comment.product = Product.objects.get(product_version=self.get_object())
            comment.save()
        return redirect('product_detail' , pk=self.kwargs.get('pk'))
    
    
  