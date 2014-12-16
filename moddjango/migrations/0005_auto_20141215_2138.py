# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moddjango', '0004_auto_20141215_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='dependencies',
            field=models.ManyToManyField(related_name='dependence', null=True, to='moddjango.Module', blank=True),
            preserve_default=True,
        ),
    ]
