from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'app_home/home.html'


class ComingSoonView(TemplateView):
    template_name = 'app_home/comingsoon.html'
