from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import ListView
from .models import Cat
from .forms import CatForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.contrib.auth import login

class  HomePageView(ListView):
    model = Cat
    template_name = 'cats/home.html'

@login_required
def CreateView(request):
    if request.method == 'POST':
        form = CatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cats/')
    else:
        form = CatForm()
    return render(request, 'cats/create.html', {'form': form})

@login_required
def EditView(request, id):
    cat = get_object_or_404(Cat, pk=id)
    form = CatForm(instance=cat)

    if (request.method == 'POST'):
        form = CatForm(request.POST, instance=cat)
        if form.is_valid():
            cat.save()
            return HttpResponseRedirect('/cats/')
    else:
        return render(request, 'cats/create.html', {'form': form, 'cat': cat})

@login_required
def DeleteView(request, id):
    cat = get_object_or_404(Cat, pk=id)
    cat.delete()
    return HttpResponseRedirect('/cats/')

def AboutView(request):
    return render(request, 'about.html')

def ContactView(request):
    return render(request, 'contact.html')

#TODO fazer template
def DonateView(request):
    return render(request, 'about.html')



