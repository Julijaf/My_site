from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


# Create your views here.


def index(request):
    return render(request, 'main/index.html', {"Title": "The main page"})


def about(request):
    return render(request, 'main/about.html')


def pricelist(request):
    return render(request, 'main/pricelist.html')


def statistics(request):
    return render(request, 'main/statistics.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def services(request):
    return render(request, 'main/services.html')


def team(request):
    return render(request, 'main/team.html')


def news(request):
    return render(request, 'main/news.html')
