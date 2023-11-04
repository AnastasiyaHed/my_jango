from django.shortcuts import render
from .models import BlogPost

def home(request):
    return render(request, 'test_app/home.html')

def about(request):
    return render(request, 'test_app/about.html')

def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'test_app/blog.html', {'blog_posts': blog_posts})