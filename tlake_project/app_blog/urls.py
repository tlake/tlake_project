from django.conf.urls import patterns, url
from app_blog.views import (BlogHomeView, PostView, )

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tlake_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', BlogHomeView.as_view(), name='app_blog-home'),
    url(r'^(?P<slug>[-\w]+)$', PostView.as_view(), name='app_blog-post_detail'),

)
