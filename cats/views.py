from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Cat
from django.contrib.auth.views import LoginView

from django.contrib.auth import login

class  HomePageView(ListView):
    model = Cat
    template_name = 'cats/home.html'

def AboutView(request):
    return render(request, 'about.html')

def ContactView(request):
    return render(request, 'contact.html')

class Login(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True



