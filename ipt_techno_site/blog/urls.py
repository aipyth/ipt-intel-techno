from django.urls import path

from .views import PostDetail, PostList, home_view


urlpatterns = [
    path('', home_view, name='home'),
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
