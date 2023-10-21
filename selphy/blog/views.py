from typing import Any, Dict
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404,resolve_url,redirect
from .models import Blogs,Comments,Author,Category
from .forms import CommentForm
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,DetailView,ListView,CreateView,UpdateView,DeleteView,FormView

class Blogview(ListView):
    model= Blogs
    template_name='blog.html'
    context_object_name='allblogs'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['latestposts']=Comments.objects.order_by('-created_at')[:5]
        
        context['authors']=Author.objects.all()
        context['category']=Category.objects.all()
        context['comments']=Comments.objects.all()
        # blogs = Blogs.objects.all()
        # for blog in blogs:
        #     for comment in blog.comments.all():
                # print(comment.name)
        return context
    
    def get_queryset(self):
        num_comment=self.request.GET.get('comment')
        aut=self.request.GET.get('categories')
        types=self.request.GET.get('type')
        queryset = Blogs.objects.all()
        if aut:
            queryset = queryset.filter(author=aut)
        if types:
            queryset = queryset.filter(category__name=types)
        
        
        return queryset

class Blogdetailview(DetailView):
    model=Blogs
    template_name='blog-details.html'
    context_object_name='blog_details'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)    
        context['latestposts']=Comments.objects.order_by('-created_at')[:5]
        context['comment_form']=CommentForm()   
        context['authors']=Author.objects.all()
        context['category']=Category.objects.all()
        return context
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        blogform = CommentForm(request.POST)
        if blogform.is_valid():
            comment = blogform.save(commit=False)
            comment.blog = self.object
            comment.save()
        return redirect('blog_detail',pk=self.object.pk)
    






# Create your views here.
# def blog(request):
#     latestposts=Comments.objects.order_by('-created_at')
#     allblogs= Blogs.objects.all()
#     context={
#         'allblogs': allblogs,
#         'latestposts': latestposts,
#     }
#     print(latestposts)  
#     return render(request,'blog.html',context=context)





# def blog_details(request,id):
#     blogform=CommentForm()
#     blog_detail=Blogs.objects.get(id=id)
#     num_comment=Comments.objects.filter(blog=blog_detail).count()
#     latestposts=Comments.objects.order_by('-created_at')
    
#     if request.method =="POST":
#         blogform=CommentForm(request.POST)
#         if blogform.is_valid():
#             comment.blog = blog_detail
#             comment=blogform.save(commit=False)
#             comment.save()
#             num_comment = Comments.objects.filter(blog=blog_detail).count()
#             blog_detail.save()
#             print(blog_detail)
#     data={
#         'blog_detail': blog_detail,
#         'blogform':blogform,
#         'num_comment': num_comment,
#         'latestposts':latestposts,
#     }
#     return render(request,'blog-details.html', data)

# class updateview(UpdateView):
#     model=Blogs
#     form_class=CommentForm
#     def get_success_url(self):
#         return resolve_url()







