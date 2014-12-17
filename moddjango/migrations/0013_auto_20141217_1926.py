# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moddjango', '0012_auto_20141217_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='dependence',
            field=models.ManyToManyField(related_name='related_dependence', null=True, to='moddjango.Module', blank=True),
            preserve_default=True,
        ),
    ]
