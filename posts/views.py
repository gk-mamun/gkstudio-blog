from django.shortcuts import render
from django.http import HttpResponse

from .models import Category, Post, Tag

# Create your views here.
def posts_view(request):

    posts = Post.objects.all()
    categories = Category.objects.all()

    context = { 'posts': posts, 'categories': categories }

    return render(request, 'posts.html', context)



def single_post_view(request, pk):

    post = Post.objects.get(id=pk)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = { 'post': post, 'categories': categories, 'tags': tags }

    return render(request, 'single.html', context)