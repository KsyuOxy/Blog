from django.shortcuts import render
from forum.models import Post


def index(request):
    data = dict()
    all_posts = Post.objects.all()
    data['posts'] = all_posts[:2]
    return render(request, 'home/index.html', context=data)
