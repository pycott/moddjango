# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moddjango', '0007_module_templates'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='urls',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
