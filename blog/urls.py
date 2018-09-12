from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('<int:post_id>/update', views.post_update, name='post_update'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('like/', views.post_like, name='like'),
    path('', views.posts_list, name='posts_list'),
]
