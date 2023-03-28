from datetime import datetime, timedelta

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User



class Tag(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name



class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.created_on >= timezone.now() - timedelta(days=1)
