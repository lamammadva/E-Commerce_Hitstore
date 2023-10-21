from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import CreateView, ListView
from .models import Core,ContactUs
from product.models import Product_version,Category,Product
from blog.models import Blogs
from .form import ContacUsForm
from django.db.models import Q
# from .form import SearchForm






class SearchView(ListView):
    model=Product
    template_name='search.html'
    context_object_name='products'
    
    def get_queryset(self):
        product2=self.request.GET.get('category')   
        product=self.request.GET.get('name')
        if product2:
            multiple=Q(Q(category__name=product2) & Q(title__icontains=product))
        else:
            multiple=Q(title__icontains=product)
        return Product.objects.filter(multiple)
       

            
        
      


# Create your views here.

class About_usView(ListView):
    model = Core
    template_name='about-us.html'
    context_object_name= 'cores'
 
    

class ContacUsView(CreateView):
    template_name='contact-us.html'
    form_class= ContacUsForm
    model=ContactUs
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['forms']=ContacUsForm()
        return context
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            comment= form.save(commit=False)
            comment.save()
        return super().post(request,*args,**kwargs)
    

def faq(request):
    return render(request,'faq.html')

class IndexView(ListView):
    model= Product
    paginate_by = 8
    template_name ='index.html'
    context_object_name='product'
    def get_queryset(self):
        cat=self.request.GET.get('categories')
        if cat:
            return Product.objects.filter(category__name=cat)
        else:
            return Product.objects.all()
    def get_context_data(self, **kwargs,):
        context= super().get_context_data(**kwargs)
        context['blogs']=Blogs.objects.order_by('-created_at')
        context['products']=Product.objects.order_by('-created_at')
        return context
    
    

# def change_language(request):
#     if request.GET.get('lang')=='az' or request.GET.get('lang')=='eng' or request.GET.get('lang')=='default':
#         path_list = request.META.get('HTTP_REFERER').split('/')
#         if request.GET.get('lang')=='deafult':
#             path_list.pop(3)
#         else:
#             path_list.insert(3,request.GET.get('lang'))
#         path='/'.join(path_list)
#         response =HttpResponseRedirect(path)
#         response.set_cookie('django_language',request.GET['lang'])
#         return response
