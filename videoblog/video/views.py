from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from video.models import Video


class VideoListView(ListView):
    model = Video