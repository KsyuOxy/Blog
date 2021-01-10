from django.urls import path, include
from .views import post_list, post_details, ajax_like


urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:post_id>/post_details', post_details, name='post_details'),
    path('<int:post_id>/like', ajax_like, name='ajax_like'),
]
