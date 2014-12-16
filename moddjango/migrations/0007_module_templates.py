# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moddjango', '0006_auto_20141215_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='templates',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
