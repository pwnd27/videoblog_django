from django.urls import path
from users.views import UserFormView


urlpatterns = [
    path('', UserFormView.as_view(), name='register'),
]