from django.contrib.auth.models import User
from rest_framework import serializers
from video.models import Video


class UserSerializer(serializers.ModelSerializer):
    videos = serializers.PrimaryKeyRelatedField(many=True, queryset=Video.objects.all())

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'videos',
        ]