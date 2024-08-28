# accounts/urls.py
from django.urls import path
from .views import RegisterView, LoginView, UserDetailView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserDetailView.as_view(), name='user_detail'),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
]
