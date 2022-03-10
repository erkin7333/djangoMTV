from django.shortcuts import render




def home_page(request):
    return render(request, 'user/home_page.html')
