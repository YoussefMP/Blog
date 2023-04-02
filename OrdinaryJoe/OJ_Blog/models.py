from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.apps import AppConfig


default_app_config = 'OJ_Blog.apps.OJ_BlogConfig'


class OJ_BlogConfig(AppConfig):
    name = 'OJ_Blog'


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='OJ_Blog/pictures', null=True, blank=True)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
