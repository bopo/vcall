# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0004_auto_20160825_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='name',
        ),
        migrations.AddField(
            model_name='contacts',
            name='content',
            field=models.TextField(null=True, verbose_name='\u8054\u7cfb\u4eba\u5185\u5bb9', blank=True),
        ),
    ]
