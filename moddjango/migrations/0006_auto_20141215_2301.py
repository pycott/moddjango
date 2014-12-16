# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moddjango', '0005_auto_20141215_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='dependencies',
        ),
        migrations.AddField(
            model_name='module',
            name='dependence',
            field=models.ManyToManyField(to='moddjango.Module', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='module',
            name='status',
            field=models.CharField(default=b'downloaded', max_length=10),
            preserve_default=True,
        ),
    ]
