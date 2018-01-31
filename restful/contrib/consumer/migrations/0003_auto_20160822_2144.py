# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0002_verification'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(default='', max_length=255, verbose_name='\u8054\u7cfb\u4eba\u59d3\u540d')),
                ('mobile', models.CharField(default='', max_length=255, verbose_name='\u8054\u7cfb\u4eba\u624b\u673a')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='contacts',
            name='mobile',
            field=models.CharField(default='', max_length=255, verbose_name='\u8054\u7cfb\u4eba\u624b\u673a'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='\u8054\u7cfb\u4eba\u59d3\u540d'),
        ),
    ]
