from django.db import models
from django.utils import timezone
from datetime import datetime
import cloudinary
from cloudinary.models import CloudinaryField

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 200)
    text = models.TextField()
    file_name = models.CharField(max_length = 50)
    data = cloudinary.models.CloudinaryField(upload_to = 'images', null = True)
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

"""
class FileNameModel(models.Model):
    file_name = models.CharField(max_length = 50)
    upload_time = models.DateTimeField(default = datetime.now)
"""
