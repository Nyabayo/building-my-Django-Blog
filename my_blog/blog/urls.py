# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Homepage
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Detailed post page
    path('add/', views.add_post, name='add_post'),  # URL for adding posts
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),  # URL for editing posts
]
