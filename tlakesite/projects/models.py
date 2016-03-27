from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone


@python_2_unicode_compatible
class Project(models.Model):
    """A model describing a project."""

    title = models.CharField(max_length=127)
    desc = models.TextField()
    site_link = models.CharField(max_length=255, null=True, blank=True)
    code_link = models.CharField(max_length=255, null=True, blank=True)
    screenshot = models.ImageField(
        upload_to="screenshots",
        null=True,
        blank=True,
    )
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Override __str__ method."""
        return "Project: {}".format(self.title)
