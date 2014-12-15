# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moddjango', '0002_auto_20141215_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='status',
            field=models.CharField(default='downloaded', max_length=10),
            preserve_default=False,
        ),
    ]
