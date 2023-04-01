from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'index.html', )


def services(request):
    return render(request, 'services.html', )


def contactus(request):
    return render(request, 'contact.html', )

def whoweare(request):
    return render(request, 'whoweare.html', )


