from django import forms
from video.models import Video
import os


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = [
            'name',
            'description',
            'file',
            'cover',
        ]

    def clean_file(self):
        file = self.cleaned_data.get('file', None)
        if file:
            ext = os.path.splitext(file.name)[1].lower()
            if ext != '.mp4':
                raise forms.ValidationError('Файл должен быть в формате MP4')
            return file