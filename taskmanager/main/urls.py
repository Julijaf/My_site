from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('pricelist', views.pricelist, name='pricelist'),
    path('statistics', views.statistics, name='statistics'),
    path('contacts', views.contacts, name='contacts'),
    path('services', views.services, name='services'),
    path('team', views.team, name='team'),
    path('news', views.news, name='news')
]
