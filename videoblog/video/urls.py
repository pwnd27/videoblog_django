from django.urls import path, include
from video import views
from video import api
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'api', api.VideoViewSet, basename='video')


urlpatterns = [
    path('', views.VideoListView.as_view(), name='list'),
    path('upload/', views.VideoCreateView.as_view(), name='upload'),
    path('<int:pk>/', views.VideoDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.VideoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.VideoDeleteView.as_view(), name='delete'),
    path('', include(router.urls)),
]