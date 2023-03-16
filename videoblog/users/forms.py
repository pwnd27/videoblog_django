from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget = forms.TextInput(
        attrs={'class':'form-control','type':'password', 'name':'password'}),
        label="Пароль")
    password2 = forms.CharField(widget = forms.TextInput(
        attrs={'class':'form-control','type':'password', 'name':'password'}),
        label="Подтверждения пароля")

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
        }
        labels = {
            'username': gettext_lazy('Имя'),
            'email': gettext_lazy('Почта')
        }
        