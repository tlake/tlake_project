from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class HomePageMessage(models.Model):
    title = models.CharField(max_length=127)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'created'

    def __str__(self):
        return "HomePageMessage: {}, {}".format(self.created, self.title)
