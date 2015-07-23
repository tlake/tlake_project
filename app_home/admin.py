from django.contrib import admin
from app_blog.models import (Post, Comment)
from app_projects.models import Project
from app_home.models import HomePageMessage

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Project)
admin.site.register(HomePageMessage)
