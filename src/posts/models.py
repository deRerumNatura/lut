from django.db import models
from django.conf import settings


class Posts(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    photo = models.ImageField(blank=True, null=True, upload_to = 'covers/')
    description = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class Likes(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    post = models.ForeignKey(Posts, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
