from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя",help_text="Введите свое имя")
    age = forms.IntegerField(label="Возраст")
    comment = forms.CharField(label="Комментарий", widget=forms.Textarea)