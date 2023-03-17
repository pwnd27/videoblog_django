from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import UserRegisterView, UserLoginView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]