from django.views.generic import ListView, DetailView
from .models import Post


class BlogHomeView(ListView):
    model = Post
    template_name = 'templates/blog.html'


class PostView(DetailView):
    model = Post
