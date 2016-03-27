# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_screenshot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='screenshot',
            field=models.ImageField(null=True, upload_to=b'screenshots', blank=True),
        ),
    ]
