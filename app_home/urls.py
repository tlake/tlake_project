from django.conf.urls import patterns, url
from app_home.views import (HomePageView, ComingSoonView, )

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tlake_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', HomePageView.as_view(), name='app_home-home'),

)
