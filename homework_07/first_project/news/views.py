from datetime import datetime

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import (HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseBadRequest,
                         HttpResponseNotFound)
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView, FormView

from .forms import UserForm, ContactForm, LoginForm, SignUpForm, CommentForm, SearchForm
from .models import News, Category, Comment
# Create your views here.
from django.views import View
from django.contrib.auth.decorators import permission_required

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = 'contact/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'registration/login.html',{'form':form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username, password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('/')
        if form.errors:
            messages.error(request, 'Your username and password didn\'t match. Please try again')
        return render(request, 'registration/login.html', {'form': form})


class MainLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('HomePage')

    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

def sign_out(request):
    logout(request)
    messages.success(request,'You have been logged out')
    return redirect('login')


#Registaration
def registration(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'registration/registration.html', { 'form': form})

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            messages.success(request,'you have sign up successfully')
            return redirect('/')
        else:
            return render(request,'registration/registration.html',{'form':form})


## CRUD
class NewView(TemplateView):
    template_name = "home.html"
    model = News
    context_object_name = "news_list"

def create_news():
    if Category.objects.all().count() == 0:
        Category.objects.create(category="Sport")
        Category.objects.create(category="Gaming")
        Category.objects.create(category="War")


class NewsGet(ListView):
    model = News
    context_object_name = "news_list"
    paginate_by = 10

  #  queryset = News.objects.filter(title__icontains='Ди')


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['Neews'] = News.objects.select_related('category').all()
        return context


class NewsCategory (ListView):
    model = News
    context_object_name = 'news_category'
    template_name = 'home.html'

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        return News.object.filter(category__slug=category_slug)



class SearchResultsView(ListView):
    model = News
    form_class = SearchForm
    context_object_name = 'news_title'
    template_name = 'search_results.html'
    paginate_by = 10

    def get_queryset(self):
        query_title = self.request.GET.get('title')
        object_list = News.objects.filter(
            Q(title__icontains = query_title)
        )
        return object_list


class NewsCreate(PermissionRequiredMixin,CreateView):
    permission_required = 'news.change_news'
    create_news()
    model = News
    fields = ('title', 'description', "category","image")


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        self.request.user.save()
        return HttpResponseRedirect('/')

    def add_news(request):
        if not request.user.has_perm('news.add_news'):
            raise PermissionDenied


class RedirectPermissionRequiredMixin(PermissionRequiredMixin,):
    login_url = reverse_lazy('UpdateView')

    def handle_no_permission(self):
        return redirect(self.get_login_url())


class UpdateNews(RedirectPermissionRequiredMixin, UpdateView):
    permission_required= 'news.change_news'
    model = News
    fields = ('title', 'description', "category", 'image')
    template_name = 'news/news_update.html'
    success_url = '/'




class DeleteNews(DeleteView):
    model = News
    success_url = '/'
    context_object_name = "item"

    def add_news(request):
        if not request.user.has_perm('news.delete_news'):
            raise PermissionDenied


class NewsDetail(RedirectPermissionRequiredMixin,DetailView):
    permission_required = 'news.view_news'
    model = News
    context_object_name = 'new'
    template_name = 'news/news_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context ["category"]  = "Life"
        context ['categories'] = Category.objects.all()
        context ['existing_comments'] = Comment.objects.order_by('-created')
        context ['comment_form'] = CommentForm()
        return context

    def post (self, request, pk, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            if request.user.is_authenticated:
                comment = comment_form.save(commit=False)
                comment.name = request.user.username
                news = self.get_object()
                comment.news = news
                comment.user = request.user
                comment.save()
                return HttpResponseRedirect(reverse_lazy('NewsDetail', kwargs={'pk': pk}))
        else:
            return render (request, 'news/news_detail',context={'comment_form':comment_form,'object': self.get_object()})




## CRUD

