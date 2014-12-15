# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moddjango', '0003_module_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='dependencies',
            field=models.ManyToManyField(to='moddjango.Module'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='module',
            name='migrate',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
