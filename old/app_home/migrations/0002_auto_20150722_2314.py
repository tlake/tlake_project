# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepagemessage',
            options={'get_latest_by': 'created'},
        ),
    ]
