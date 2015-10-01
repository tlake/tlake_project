# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20151001_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='code_link',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='site_link',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
