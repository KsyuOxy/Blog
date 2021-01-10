from django.shortcuts import render
from .models import Post
from django.http import Http404


def post_list(request):
    data = dict()
    all_posts = Post.objects.all()
    data['posts'] = all_posts
    return render(request, 'forum/post_list.html', context=data)


def post_details(request, post_id: int):
    data = dict()
    posts = Post.objects.filter(id=post_id)
    if not posts.exists():
        raise Http404
    post = Post.objects.get(id=post_id)
    data['post'] = post
    return render(request, 'forum/post_details.html', context=data)
