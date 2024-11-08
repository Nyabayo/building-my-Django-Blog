# my_blog/urls.py (or project-level urls.py)
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('blog.urls')),  # Include your blog app's URLs
]
