from django.urls import path

from .views import PostDetail, PostList


urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
