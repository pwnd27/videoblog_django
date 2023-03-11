from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    description = models.TextField()
    url = models.FileField(max_length=50, null=True, blank=True)
    cover = models.ImageField(max_length=50, null=True, blank=True)
