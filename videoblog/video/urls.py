from django.urls import path
from video import views
from video import api


urlpatterns = [
    path('', views.VideoListView.as_view(), name='list'),
    path('upload/', views.VideoCreateView.as_view(), name='video-upload'),
    path('<int:pk>/', views.VideoDetailView.as_view(), name='video-detail'),
    path('update/<int:pk>/', views.VideoUpdateView.as_view(), name='video-update'),
    path('delete/<int:pk>/', views.VideoDeleteView.as_view(), name='video-delete'),
    path('api/', api.VideoListAPIView.as_view(), name='video-list-api'),
    path('api/<int:pk>/', api.VideoDetailAPIView.as_view(), name='video-detail-api'),
]