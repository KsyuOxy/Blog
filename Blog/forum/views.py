from django.shortcuts import render
from .models import Post
from django.http import Http404, JsonResponse
from django.core.paginator import Paginator


def post_list(request):
    data = dict()
    all_posts = Post.objects.all()

    paginator = Paginator(all_posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # data['posts'] = all_posts
    data['page_obj'] = page_obj
    return render(request, 'forum/post_list.html', context=data)


def post_details(request, post_id: int):
    data = dict()
    posts = Post.objects.filter(id=post_id)
    if not posts.exists():
        raise Http404
    post = Post.objects.get(id=post_id)
    data['post'] = post
    # data['liked'] = post.likes.filter(like_list=request.user)
    return render(request, 'forum/post_details.html', context=data)


def ajax_like(request, post_id):
    response = dict()
    response['status'] = 'error'
    if request.user.is_authenticated:
        posts = Post.objects.filter(id=post_id)
        if not posts.exists():
            raise Http404
        post = Post.objects.get(id=post_id)
        like_action = request.GET.get('like_action')
        if like_action == 'add':
            post.likes.add(request.user)
            response['status'] = 'ok'
        elif like_action == 'remove':
            post.likes.remove(request.user)
            response['status'] = 'ok'

    return JsonResponse(response)
