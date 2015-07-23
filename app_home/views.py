from django.views.generic import TemplateView, ListView
from app_home.models import HomePageMessage


class HomePageView(ListView):
    model = HomePageMessage
    template_name = 'app_home/home.html'


class ComingSoonView(TemplateView):
    template_name = 'app_home/comingsoon.html'
