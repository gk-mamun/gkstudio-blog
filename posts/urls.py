from django.urls import path

from .views import (
    posts_view,
    single_post_view,
)

urlpatterns = [
    path('', posts_view, name="posts"),
    path('post/<str:pk>/', single_post_view, name="single"),
]
