from django.urls import path
from video.views import VideoListView, VideoCreateView, VideoDetailView, VideoUpdateView, VideoDeleteView


urlpatterns = [
    path('', VideoListView.as_view(), name='list'),
    path('upload/', VideoCreateView.as_view(), name='video-upload'),
    path('<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('update/<int:pk>/', VideoUpdateView.as_view(), name='video-update'),
    path('delete/<int:pk>/', VideoDeleteView.as_view(), name='video-delete'),
]