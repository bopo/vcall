# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0006_customuser_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='content',
        ),
        migrations.AddField(
            model_name='contacts',
            name='mobile',
            field=models.CharField(default='', max_length=255, verbose_name='\u8054\u7cfb\u4eba\u624b\u673a'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='\u8054\u7cfb\u4eba\u59d3\u540d'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='status',
            field=model_utils.fields.StatusField(default='0', max_length=100, verbose_name='status', no_check_for_status=True, choices=[(0, 'dummy')]),
        ),
        migrations.AddField(
            model_name='contacts',
            name='status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status'),
        ),
        migrations.AddField(
            model_name='friends',
            name='friend',
            field=models.ForeignKey(to='consumer.Contacts'),
        ),
        migrations.AddField(
            model_name='friends',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
