# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0007_auto_20160829_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='mobile',
            field=models.CharField(default='', unique=True, max_length=25, verbose_name='\u8054\u7cfb\u4eba\u624b\u673a'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='\u8054\u7cfb\u4eba\u59d3\u540d'),
        ),
    ]
