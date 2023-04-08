from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.apps import AppConfig
from ckeditor_uploader.fields import RichTextUploadingField


default_app_config = 'OJ_Blog.apps.OJ_BlogConfig'


class OJBlogConfig(AppConfig):
    name = 'OJ_Blog'


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='OJ_Blog/pictures', null=True, blank=True)
    content = RichTextUploadingField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now, db_index=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def get_absolute_utl(self):
        return reverse("post-id", args=[str(self.title)])
