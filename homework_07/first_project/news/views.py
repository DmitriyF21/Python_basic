from datetime import datetime

from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseBadRequest,
                         HttpResponseNotFound)
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView

from .forms import UserForm
from .models import News, Category
# Create your views here.
from django.views import View


class NewView(TemplateView):
    template_name = "home.html"
    model = News
    context_object_name = "News_list"

def create_news():
    if Category.objects.all().count() == 0:
        Category.objects.create(category="Sport")
        Category.objects.create(category="Gaming")
        Category.objects.create(category="War")


class NewsCreate(CreateView):
    create_news()
    model = News
    fields = ('title', 'description',"category")
    paginate_by = 2
    success_url = '/'


class NewsGet(ListView):
    model = News
    context_object_name = "News_list"
  #  queryset = News.objects.filter(title__icontains='Ди')


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context ['some_var'] = 'some variables'
        return context


class UpdateNews(UpdateView):
    model = News
    fields = ('title', 'description',"category")
    success_url = '/'


class DeleteNews(DeleteView):
    model = News
    success_url = '/'
    context_object_name = "item"


class NewsDetail(DetailView):
    model = News

