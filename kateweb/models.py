import uuid

from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit, ResizeToFill
from PIL import Image
from datetime import datetime

now = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")

class MyInfo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    img = models.ImageField(default='default.jpg', upload_to='course_images')

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=1024)
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFill(300, 200)], format='JPEG',
                                options={'quality': 90})
    tags = models.CharField(max_length=250)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title



class AlbumImage(models.Model):
    image = ProcessedImageField(upload_to='albums',
                                processors=[ResizeToFit(width=1280)],
                                format='JPEG',
                                options={'quality': 70})
    thumb = ProcessedImageField(upload_to='albums',
                                processors=[ResizeToFill(200, 200)],
                                format='JPEG',
                                options={'quality': 80})
    album = models.ForeignKey('album', on_delete=models.PROTECT)
    alt = models.CharField(max_length=255, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    slug = models.SlugField(max_length=70, default=uuid.uuid4, editable=False)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return str(self.alt) + ' = photo from album = ' + str(self.album)