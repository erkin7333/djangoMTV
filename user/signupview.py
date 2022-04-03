from django.shortcuts import reverse, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomeUserCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin




# Djangoni o'zinii ro'yxatdan o'tish tizimi

class SignupView(generic.CreateView):
    template_name = 'registr/signup.html'
    form_class = CustomeUserCreateForm

    def get_success_url(self):
        return reverse("user:login")


