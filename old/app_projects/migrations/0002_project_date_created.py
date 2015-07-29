# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 17, 55, 39, 261718, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
