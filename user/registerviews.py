from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.generic import View
from .forms import RegisterModelForm, Login_User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
User = get_user_model()



class UserRegisterView(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

    def get(self, request):
        form = RegisterModelForm()
        context = {
            'form': form
        }
        return render(request, 'registr/registr.html', context)

    def post(self, request):
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            del data['confirm']
            user = User(**data)
            user.password = make_password(data['password'])
            user.save()
            return redirect('user:login')
        else:
            form = RegisterModelForm()
            context = {
                'form': form
            }
        return render(request, 'registr/registr.html', context)

def user_login(request):
    form = Login_User()
    if request.method == 'POST':
        form = Login_User(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('user:home')
            form.add_error('password', "Username va/yoki parol noto'g'ri.")
    return render(request, 'registr/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('user:home')