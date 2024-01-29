from django import forms
from .models import  News
from django.forms import ModelForm


class UserForm(forms.Form):
    name = forms.CharField(label="Имя",help_text="Введите свое имя")
    age = forms.IntegerField(label="Возраст")
    comment = forms.CharField(label="Комментарий", widget=forms.Textarea)


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'category')


class LoginForm(forms.ModelForm):
    login = forms.CharField()
    password = forms.CharField()




