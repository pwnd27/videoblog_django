from rest_framework import viewsets
from rest_framework import status
from video.models import Video
from video.serializers import VideoSerializer
from rest_framework.response import Response
from rest_framework import permissions
from video.permissions import IsOwnerOrReadOnly
import os


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, instance):
        instance.save(user=self.request.user)

    def perform_destroy(self, instance):
        video_path = instance.file.path
        cover_path = instance.cover.path
        if os.path.isfile(cover_path):
            os.remove(cover_path)
        if os.path.isfile(video_path):
            os.remove(video_path)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_update(self, instance):
        new_file = self.request.data.get('file', None)
        new_cover = self.request.data.get('cover', None)
        if new_file:
            instance.file = new_file
        if new_cover:
            instance.cover = new_cover
        instance.save()
        return Response(instance.data)
