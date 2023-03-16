from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import UserRegisterView, UserLoginView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]