from django.db import models

# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=100)
    video_url = models.URLField()

    def __str__(self):
        return self.name
