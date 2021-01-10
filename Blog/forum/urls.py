from django.urls import path, include
from .views import post_list, post_details


urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:post_id>/post_details', post_details, name='post_details'),
]
