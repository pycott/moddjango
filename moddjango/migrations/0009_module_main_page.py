# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moddjango', '0008_module_urls'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='main_page',
            field=models.CharField(default=False, max_length=255),
            preserve_default=False,
        ),
    ]
