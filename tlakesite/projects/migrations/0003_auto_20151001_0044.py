# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20151001_0728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='link',
            new_name='code_link',
        ),
        migrations.AddField(
            model_name='project',
            name='site_link',
            field=models.URLField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
