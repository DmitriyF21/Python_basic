from datetime import datetime

from django.contrib.auth import logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.http import (HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseBadRequest,
                         HttpResponseNotFound)
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView, FormView

from .forms import UserForm, ContactForm, LoginForm, SignUpForm
from .models import News, Category
# Create your views here.
from django.views import View


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = 'contact/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


#Registaration
def registration(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'registration/registration.html', { 'form': form})


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = "registration/login.html"

    def form_valid(self, form):
        super().form_valid(form)
        login = form.cleaned_data.get('login')
        password = form.cleaned_data.get('password')
        user = authenticate(username=login, password=password)
        return redirect('/')


class MainLogoutView(LogoutView):
    """Представление, для выхода из логина"""
    next_page = reverse_lazy('home')



## CRUD
class NewView(TemplateView):
    template_name = "home.html"
    model = News
    context_object_name = "News_list"

def create_news():
    if Category.objects.all().count() == 0:
        Category.objects.create(category="Sport")
        Category.objects.create(category="Gaming")
        Category.objects.create(category="War")


class NewsGet(ListView):
    model = News
    context_object_name = "news_list"

  #  queryset = News.objects.filter(title__icontains='Ди')


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['categories'] = Category.objects.all()
        return context


class NewsCreate(CreateView):
    create_news()
    model = News
    fields = ('title', 'description',"category")
    paginate_by = 2
    success_url = '/'


class UpdateNews(UpdateView):
    model = News
    fields = ('title', 'description',"category")
    template_name = 'news/news_update.html'
    success_url = '/'



class DeleteNews(DeleteView):
    model = News
    success_url = '/'
    context_object_name = "item"


class NewsDetail(DetailView):
    model = News

## CRUD