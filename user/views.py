from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CustomUser, Agent
from .forms import CustomUserForm, CustomUserModelForm, UserCreationForm
from agents.mixins import OrganisorAndLoginRequiredMixin



# /// CRUD Amallari == CREATEVIEW, RETRIEVEVIEW, UPDATEVIEW, DELETEVIEW,  ++ LISTVIWIEW  \\\ >


class LandingPageView(TemplateView):
    template_name = 'user/home_page.html'

# < /// Bazadan malimotni ListView bn olish usuli \\\ >
class UserListView(LoginRequiredMixin, ListView):
    template_name = 'user/customuser.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        user = self.request.user
        ## Butun tashkilot uchun dastlabki so'rovlar to'plami
        if user.is_organisor:
            queryset = CustomUser.objects.filter(organisation=user.userprofile)
        else:
            queryset = CustomUser.objects.filter(organisation=user.agent.organisation)
            ## Tizimga kirgan agent uchun filtr
            queryset = queryset.filter(agent__user=self.request.user)
        return queryset

# < /// Barcha Userlarni funksiya bn chiqarish uchun yozilgan kodlar  \\\ >
def customuser_list(request):
    user_list = CustomUser.objects.all()
    context = {
        'user_list': user_list
    }
    return render(request, 'user/customuser.html', context)

# < /// Userni o'ziga tegishli barcha malumotini batafsil ko'rinish usuli DETAILVIEW yordamida \\\ >

class UserDeatailView(LoginRequiredMixin, DetailView):
    template_name = 'user/custom_detail.html'
    context_object_name = 'detail'

    def get_queryset(self):
        user = self.request.user
        ## Butun tashkilot uchun dastlabki so'rovlar to'plami
        if user.is_organisor:
            queryset = CustomUser.objects.filter(organisation=user.userprofile)
        else:
            queryset = CustomUser.objects.filter(organisation=user.agent.organisation)
            ## Tizimga kirgan agent uchun filtr
            queryset = queryset.filter(agent__user=self.request.user)
        return queryset

# < /// User detail uchun yozilgan kodlar Funksiya usuli \\\ >
def customuser_detail(request, pk):
    detail = CustomUser.objects.get(id=pk)
    context = {
        'detail': detail
    }
    return render(request, 'user/custom_detail.html', context)

# < /// Bazaga CreateView yordamida user Qo'shish usuli \\\ >
class UserCreateView(OrganisorAndLoginRequiredMixin, CreateView):
    template_name = 'user/customuser_create.html'
    form_class = CustomUserModelForm

    def get_success_url(self):
        return reverse("user:home")

    def form_valid(self, form):
        # Elektron pochtaga xabar jo'natish
        send_mail(
            subject="Etakchi user yaratildi",
            message="Yangi rahbarni ko'rish uchun saytga o'ting",
            from_email=["erkinnajimov90@gmail.com"],
            recipient_list=["erkinnajimov90@gmail.com"]
        )
        return super(UserCreateView, self).form_valid(form)

# < /// ModelForm uchun yozilgan kod Bu kod Bazaga user qo'shish uchun ishlatiladi Fuksiya usulda yozilgan \\\\>
def user_create(request):
    form = CustomUserModelForm()
    if request.method == 'POST':
        form = CustomUserModelForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = form.cleaned_data['agent']
            CustomUser.objects.create(first_name=first_name, last_name=last_name, age=age, agent=agent)
            return redirect("user:customuser_list")
    else:
        form = CustomUserModelForm()
    context = {
        'form': form
    }

    return render(request, 'user/customuser_create.html', context)



# < /// User malumotlarini Form bn yangilash uzgartirish \\\ >
# def user_update(request, pk):
#     update = CustomUser.objects.get(id=pk)
#     form = CustomUserForm()
#     if request.method == 'POST':
#         form = CustomUserForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             update.first_name = first_name
#             update.last_name = last_name
#             update.age = age
#             update.save()
#             return redirect("user:customuser_list")
#     else:
#         form = CustomUserForm()
#     context = {
#         'update': update,
#         'form': form
#     }
#     return render(request, 'user/user_update.html', context)


# < /// User malumotlarini ModelForm bn yangilash uzgartirish \\\ >

# < /// UpdateView yordamida Userni malumotlarini yangilash uzgartirish usuli \\\ >
class UserUpdateView(OrganisorAndLoginRequiredMixin, UpdateView):
    template_name = 'user/user_update.html'
    form_class = CustomUserModelForm

    def get_queryset(self):
        user = self.request.user
           ## Tizimga kirgan agent uchun filtr
        return CustomUser.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse("user:user_detail", kwargs={'pk': pk})


# < /// Userni malumotlarini yangilash o'zgartirish kodi Funksiya usulida \\\ >
def user_update(request, pk):
    update = CustomUser.objects.get(id=pk)
    form = CustomUserModelForm(instance=update)
    if request.method == "POST":
        form = CustomUserModelForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('user:customuser_list')
    else:
        form = CustomUserModelForm(instance=update)
    context = {
        'form': form,
        'update': update
    }
    return render(request, 'user/user_update.html', context)





# < /// Userni ochirish \\\ >
def user_delete(request, id):
    delet = CustomUser.objects.get(id=id)
    delet.delete()
    return redirect('user:customuser_list')




# < ///  Form uchun yozilgan kod ///>
# def user_create(request):
#     form = CustomUserForm()
#     if request.method == 'POST':
#         form = CustomUserForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             CustomUser.objects.create(first_name=first_name, last_name=last_name, age=age, agent=agent)
#             return redirect("user:customuser_list")
#     else:
#         form = CustomUserForm()
#     context = {
#         'form': form
#     }
#
#     return render(request, 'user/customuser_create.html', context)

