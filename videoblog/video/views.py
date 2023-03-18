from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from video.models import Video
from django.urls import reverse_lazy
from video.forms import VideoForm
from django.contrib.auth.mixins import LoginRequiredMixin
import os


class VideoListView(ListView):
    model = Video

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.exclude(file='')


class VideoDetailView(DetailView):
    model = Video
    template_name = 'video/video_detail.html'


class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'video/video_upload.html'
    success_url = reverse_lazy('list')
    login_url = '/users/login/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class VideoUpdateView(LoginRequiredMixin, UpdateView):
    model = Video
    login_url = '/users/login/'
    template_name = 'video/video_update.html'
    fields = [
        'name',
        'description',
        'file',
        'cover',
    ]

    def form_valid(self, form):
        obj = self.get_object()
        new_file = form.cleaned_data.get('file', None)
        new_cover = form.cleaned_data.get('cover', None)

        if new_file:
            if os.path.isfile(obj.file.path):
                os.remove(obj.file.path)
            
        if new_cover:
            if os.path.isfile(obj.cover.path):
                os.remove(obj.cover.path)
        
        return super().form_valid(form)


class VideoDeleteView(LoginRequiredMixin, DeleteView):
    model = Video
    login_url = '/users/login/'
    template_name = 'video/video_delete.html'
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        obj = self.get_object()
        if obj.file:
            os.remove(obj.file.path)
        if obj.cover:
            os.remove(obj.cover.path)
        return super().form_valid(form)