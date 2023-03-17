from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, CreateView
from video.models import Video
from django.urls import reverse_lazy
from video.forms import VideoForm
from django.contrib.auth.mixins import LoginRequiredMixin

class VideoListView(ListView):
    model = Video


class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'video/upload_video.html'
    success_url = reverse_lazy('list')
    login_url = '/users/login/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)