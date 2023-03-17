from django.urls import path
from video.views import VideoListView, VideoCreateView


urlpatterns = [
    path('', VideoListView.as_view(), name='list'),
    path('upload/', VideoCreateView.as_view(), name='upload'),
]