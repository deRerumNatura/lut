from django.db import models


class Posts(models.Model):
    photo = models.ImageField(blank=True, null=True, upload_to = 'covers/  ')
    description = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
