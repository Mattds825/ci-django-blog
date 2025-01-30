from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Post

# def my_blog(request):
#     return HttpResponse("Hello, welcome to my blog!")

# Create your views here.

class PostList(generic.ListView):
    # model = Post
    queryset = Post.objects.all().filter(status=1).order_by("-created_on")
    template_name = "post_list.html"