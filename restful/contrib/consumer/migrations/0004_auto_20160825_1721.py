# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0003_auto_20160822_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='alipay',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='chinese_zodiac',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='qq',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='qrcode',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='total',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='zodiac',
        ),
    ]
