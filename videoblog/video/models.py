from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=50, db_index=True)
    description = models.TextField()
    url = models.FileField(upload_to='videos/%Y/%m/%d/', max_length=50, null=True, blank=True)
    cover = models.ImageField(upload_to='covers/%Y/%m/%d/', max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name