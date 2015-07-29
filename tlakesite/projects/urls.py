from django.conf.urls import patterns, url
from .views import ProjectsListView


urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'tlake_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    '',
    url(r'^$', ProjectsListView.as_view(), name='projects_list'),

)
