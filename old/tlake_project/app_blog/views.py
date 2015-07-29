from django.views.generic import ListView, DetailView
from app_blog.models import Post


class BlogHomeView(ListView):
    model = Post
    template_name = 'app_blog/home.html'


class PostView(DetailView):
    model = Post
