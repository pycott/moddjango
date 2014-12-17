# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moddjango', '0009_module_main_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='main_page',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
