# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0005_auto_20160826_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(db_index=True, max_length=25, verbose_name='\u7528\u6237\u59d3\u540d', blank=True),
        ),
    ]
