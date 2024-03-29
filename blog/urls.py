from django.urls import path
from . import views

from .views import *


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.post_new_or_edit, name='post_new'),
    path('post/<int:pk>/edit/', views.post_new_or_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
]