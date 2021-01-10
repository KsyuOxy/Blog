from django.shortcuts import render
from forum.models import Post


def index(request):  # отбирает последние два поста, исключая draft
    data = dict()
    posts = []
    all_posts = Post.objects.all()
    for post in all_posts:
        if not post.draft and len(posts) < 3:
            posts.append(post)
    data['posts'] = posts
    return render(request, 'home/index.html', context=data)
