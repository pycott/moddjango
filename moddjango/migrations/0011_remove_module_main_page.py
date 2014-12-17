# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moddjango', '0010_auto_20141217_0753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='main_page',
        ),
    ]
