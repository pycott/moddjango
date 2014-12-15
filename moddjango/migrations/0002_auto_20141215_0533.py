# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moddjango', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='desc',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.CharField(unique=True, max_length=255),
            preserve_default=True,
        ),
    ]
