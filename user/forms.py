from django import forms
from .models import CustomUser
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
User = get_user_model()
from django.utils.translation import gettext_lazy as _



class RegisterModelForm(forms.ModelForm):
    password = forms.CharField(max_length=30, widget=forms.PasswordInput, required=True,
                               validators=[MinLengthValidator(3), MaxLengthValidator(15)])

    confirm = forms.CharField(max_length=30, widget=forms.PasswordInput, required=True,
                               validators=[MinLengthValidator(3), MaxLengthValidator(15)])

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm')
        labels = {
            "username": "Foydalanuvchi nomi",
            "password": "Parol",
            "confirm": "Parolni tasdiqlang",
        }

class CustomeUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField}


class Login_User(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)


class CustomUserModelForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'age', 'agent']



class CustomUserForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    age = forms.IntegerField(min_value=0)


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField}