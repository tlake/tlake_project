from django.views.generic import ListView
from .models import Project


class ProjectsListView(ListView):
    queryset = Project.objects.order_by("-date_created")
    template_name = 'projects_list.html'
