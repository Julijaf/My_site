from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'news.html', {'form': form})


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
