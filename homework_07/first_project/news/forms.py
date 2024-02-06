from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import FormView

from .models import  News
from django.forms import ModelForm


class UserForm(forms.Form):
    name = forms.CharField(label="Имя",help_text="Введите свое имя")
    age = forms.IntegerField(label="Возраст")
    comment = forms.CharField(label="Комментарий", widget=forms.Textarea)


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField()

    def send_email(self):
        pass


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'category')


class LoginForm(AuthenticationForm):
    login = forms.CharField()
    password = forms.CharField(widget= forms.PasswordInput)

    class Meta:
        fields = ['username','password']


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','password1','password2']

