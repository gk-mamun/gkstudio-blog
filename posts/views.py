from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def posts_view(response):

    context = {}

    return render(response, 'posts.html', context)