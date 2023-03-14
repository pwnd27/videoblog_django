from django.urls import path
from video.views import VideoListView


urlpatterns = [
    path('', VideoListView.as_view(), name='list'),
]