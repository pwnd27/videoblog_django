from rest_framework import serializers
from video.models import Video


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = (
            'url',
            'id',
            'user',
            'name',
            'description',
            'file',
            'cover',
        )