from django.urls import path
from .views import get_posts, post_detail, create_or_edit_post

urlpatterns = [
    path('', get_posts, name='get_posts'),
    path('<int:path_id>', post_detail, name='post_detail'),
    path('new/', create_or_edit_post, name='new_post'),
    path('<int:path_id>/edit/', create_or_edit_post, name='edit_post'),
]