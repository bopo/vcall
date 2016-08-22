# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('mobile', models.CharField(default='', unique=True, max_length=255, verbose_name='\u624b\u673a\u53f7')),
                ('verify', models.CharField(default='', max_length=255, verbose_name='\u9a8c\u8bc1\u7801')),
            ],
            options={
                'verbose_name': 'Verification',
                'verbose_name_plural': 'Verification',
            },
        ),
    ]
