from django.conf.urls import patterns, url
from decohere-me.views import (HomePageView)

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='decohere-me-home'),
)
