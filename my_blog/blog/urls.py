# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Homepage
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Detailed post page
]
