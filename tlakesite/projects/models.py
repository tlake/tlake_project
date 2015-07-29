from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Project(models.Model):
    title = models.CharField(max_length=127)
    desc = models.TextField()
    link = models.URLField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Project: {}".format(self.title)
