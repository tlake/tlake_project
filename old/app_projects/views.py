from django.views.generic import ListView
from app_projects.models import Project


class ProjectsListView(ListView):
    model = Project
    template_name = 'app_projects/projects_list.html'
