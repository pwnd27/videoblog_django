from rest_framework import generics
from video.models import Video
from video.serializers import VideoSerializer


class VideoAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer