from django.views import generic
from django.shortcuts import render

from .models import Post, SliderPost


def home_view(request):
    slider_posts = SliderPost.objects.filter(active=True)
    posts = Post.objects.filter(status=1).order_by('-created_on')[:9]
    context = {
        'slider_posts': slider_posts,
        'posts_preview': posts,
    }
    return render(request, 'blog/index.html', context)


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_list.html'
    paginate_by = 21


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
