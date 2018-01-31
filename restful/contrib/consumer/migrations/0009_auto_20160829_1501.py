# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0008_auto_20160829_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='owner',
        ),
        migrations.AddField(
            model_name='contacts',
            name='owner',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
