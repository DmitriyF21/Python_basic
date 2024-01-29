from django.urls import path,re_path
from django.views.generic import TemplateView, UpdateView

from . import views
from .views import  NewView, NewsDetail, NewsGet, UpdateNews, \
    DeleteNews, NewsCreate

urlpatterns = [
    path("", NewView.as_view(template_name="home.html"), name="HomePage"),
    path("create/", NewsCreate.as_view(), name="NewsCreate"),
    path("get/", NewsGet.as_view(), name="NewsGet"),
    path("get/<int:pk>", NewsDetail.as_view(), name="NewsDetail"),
    path("update/<int:pk>", UpdateNews.as_view(), name="UpdateView"),
    path("delete/<int:pk>", DeleteNews.as_view(), name="DeleteProduct"),
]
