from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='videos')
    name = models.CharField(max_length=50, db_index=True)
    description = models.TextField()
    file = models.FileField(upload_to='videos/%Y/%m/%d/', max_length=50, null=True, blank=True)
    cover = models.ImageField(upload_to='covers/%Y/%m/%d/', max_length=50, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('video-detail', args=[str(self.id)])

    def __str__(self):
        return self.name