from datetime import  datetime

from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

from django.db import models
from django.utils.translation import gettext_lazy as _




class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural="categories"
        app_label = 'news'


class News(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=10000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img/", blank=True)

    class Meta:
        verbose_name_plural = "news"
        app_label = 'news'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('NewsDetail', args=[str(self.pk)])


class Comment (models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE,related_name='comments')
    comment = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name