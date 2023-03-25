from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import UserRegisterView, UserLoginView
from users import api


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/', api.UserList.as_view(), name='users-list-api'),
    path('api/<int:pk>', api.UserDetail.as_view(), name='user-detail-api'),
]