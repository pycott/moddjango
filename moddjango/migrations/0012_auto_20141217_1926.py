# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moddjango', '0011_remove_module_main_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='dependence',
            field=models.ManyToManyField(related_name='related_dependendce', null=True, to='moddjango.Module', blank=True),
            preserve_default=True,
        ),
    ]
