from django.shortcuts import render
from blog.models import Post, Comment

# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts
    }
    return render(request, 'blog/index.html', context)

def blog_category(request, category):
    post = Post.objects.filter(
        categories__name__contains=category
    ).order_by('-created_on')
    context = {
        "category": category,
        "post": post
    }
    return render(request, 'blog/category.html', context)