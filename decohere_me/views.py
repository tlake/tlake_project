#from decohere-me.models import ()
from django.views.generic import TemplateView


class HomePageView(TemplateView):

    template_name = 'decohere-me/home.html'
