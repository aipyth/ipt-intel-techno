from django.views import generic
from django.shortcuts import render

from .models import Post


def home_view(request):
    context = {
        'slider_posts': Post.objects.filter(status=1).order_by('-created_on')[:3],
        'posts_preview': Post.objects.filter(status=1).order_by('-created_on')[:9]
    }
    return render(request, 'blog/index.html', context)


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_list.html'
    paginate_by = 20


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
