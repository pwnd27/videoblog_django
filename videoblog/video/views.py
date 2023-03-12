from django.shortcuts import render, HttpResponse
from video.models import Video

def get_list(request):
    videos = Video.objects.all()
    return render(request, 'video/videos.html', context={'videos': videos})