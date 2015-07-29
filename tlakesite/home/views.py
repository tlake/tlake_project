from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import HomePageMessage


class HomePageView(ListView):
    model = HomePageMessage
    template_name = 'home.html'
