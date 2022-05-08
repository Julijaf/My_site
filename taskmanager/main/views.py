from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import MessageForm
from .models import Message


def index(request):
    return render(request, 'main/index.html', {"Title": "The main page"})


def about(request):
    return render(request, 'main/about.html')


def pricelist(request):
    return render(request, 'main/pricelist.html')


def statistics(request):
    return render(request, 'main/statistics.html')


def contacts(request):
    error = ""
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news')
        else:
            error = "WASTED"



    form = MessageForm()

    return render(request, 'main/contacts.html', {'form': form, 'error': error})


def services(request):
    return render(request, 'main/services.html')


def team(request):
    return render(request, 'main/team.html')


def news(request):
    news = Message.objects.all()
    return render(request, 'main/news.html', {'news': news})
