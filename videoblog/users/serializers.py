from django.contrib.auth.models import User
from rest_framework import serializers
from video.models import Video


class UserSerializer(serializers.HyperlinkedModelSerializer):
    videos = serializers.HyperlinkedRelatedField(many=True, view_name='video-detail', read_only=True)

    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'username',
            'videos',
        ]