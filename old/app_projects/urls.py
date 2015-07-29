from django.conf.urls import patterns, url
from app_projects.views import ProjectsListView


urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'tlake_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    '',
    url(r'^$', ProjectsListView.as_view(), name='app_projects-projects_list'),

)
