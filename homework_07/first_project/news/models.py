from datetime import  datetime

from django.urls import reverse
from django.utils import timezone

from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural="categories"
        app_label = 'news'


class News(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/images/",blank=True)

    class Meta:
        verbose_name_plural = "news"
        app_label = 'news'



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

