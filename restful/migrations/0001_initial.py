# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u6e20\u9053\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u5b89\u88c5\u6e20\u9053',
                'verbose_name_plural': '\u5b89\u88c5\u6e20\u9053',
            },
        ),
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('badge', models.IntegerField(verbose_name='\u5b89\u88c5\u6807\u8bb0')),
                ('timeZone', models.CharField(max_length=255, verbose_name='\u8bbe\u5907\u65f6\u533a')),
                ('deviceToken', models.CharField(max_length=255, verbose_name='\u8bbe\u5907\u4ee4\u724c')),
                ('installationId', models.CharField(max_length=255, verbose_name='\u8bbe\u5907\u7f16\u53f7')),
                ('deviceType', models.CharField(max_length=10, verbose_name='\u8bbe\u5907\u7c7b\u578b', choices=[('ios', 'IOS'), ('android', 'Android')])),
                ('channel', models.CharField(max_length=10, verbose_name='\u63a8\u5e7f\u6e20\u9053', choices=[('1000', '\u5b98\u7f51'), ('1001', '91\u52a9\u624b'), ('1002', '\u767e\u5ea6'), ('1003', '\u5b89\u5353'), ('1004', '\u8c4c\u8c46\u835a'), ('1005', '\u5e94\u7528\u5b9d'), ('1006', '360'), ('1007', '\u5e94\u7528\u6c47'), ('1008', '\u9b45\u65cf'), ('1009', 'N\u591a\u7f51'), ('1010', 'PP\u52a9\u624b'), ('1011', '\u6dd8\u5b9d'), ('1012', '\u673a\u950b\u7f51'), ('1013', '\u91d1\u7acb'), ('1014', '\u5c0f\u7c73'), ('1015', '\u534e\u4e3a'), ('1016', '\u641c\u72d7'), ('1017', '\u5b89\u667a'), ('1018', '\u6c83\u5546\u5e97'), ('1019', 'itools'), ('1020', '\u7535\u4fe1\u7231\u6e38\u620f'), ('1021', '\u4f18\u4ebf\u5e02\u573a'), ('1022', '\u5e94\u7528\u8d1d'), ('1023', 'googleplay'), ('1024', '\u5b89\u7c89\u7f51')])),
            ],
            options={
                'verbose_name': '\u5b89\u88c5\u7edf\u8ba1',
                'verbose_name_plural': '\u5b89\u88c5\u7edf\u8ba1',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pics_url', models.ImageField(upload_to=b'', null=True, verbose_name='\u56fe\u7247')),
                ('ordering', models.PositiveIntegerField(verbose_name='\u6392\u5e8f')),
                ('summary', models.CharField(max_length=200, verbose_name='\u56fe\u7247\u63cf\u8ff0', blank=True)),
            ],
            options={
                'verbose_name': '\u5f00\u673a\u56fe\u7247',
                'verbose_name_plural': '\u5f00\u673a\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('version', models.CharField(default='1.0.0', max_length=10, verbose_name='\u7248\u672c\u53f7')),
                ('install', models.FileField(upload_to='install', null=True, verbose_name='\u5b89\u88c5\u8fde\u63a5')),
                ('sha1sum', models.CharField(max_length=64, verbose_name='\u6587\u4ef6\u9a8c\u8bc1\u7801')),
                ('channel', models.CharField(max_length=10, verbose_name='\u63a8\u5e7f\u6e20\u9053', choices=[('1000', '\u5b98\u7f51'), ('1001', '91\u52a9\u624b'), ('1002', '\u767e\u5ea6'), ('1003', '\u5b89\u5353'), ('1004', '\u8c4c\u8c46\u835a'), ('1005', '\u5e94\u7528\u5b9d'), ('1006', '360'), ('1007', '\u5e94\u7528\u6c47'), ('1008', '\u9b45\u65cf'), ('1009', 'N\u591a\u7f51'), ('1010', 'PP\u52a9\u624b'), ('1011', '\u6dd8\u5b9d'), ('1012', '\u673a\u950b\u7f51'), ('1013', '\u91d1\u7acb'), ('1014', '\u5c0f\u7c73'), ('1015', '\u534e\u4e3a'), ('1016', '\u641c\u72d7'), ('1017', '\u5b89\u667a'), ('1018', '\u6c83\u5546\u5e97'), ('1019', 'itools'), ('1020', '\u7535\u4fe1\u7231\u6e38\u620f'), ('1021', '\u4f18\u4ebf\u5e02\u573a'), ('1022', '\u5e94\u7528\u8d1d'), ('1023', 'googleplay'), ('1024', '\u5b89\u7c89\u7f51')])),
                ('platform', models.CharField(default='android', max_length=50, verbose_name='APP\u5e73\u53f0', choices=[('ios', 'IOS'), ('android', 'Android')])),
            ],
            options={
                'verbose_name': '\u7248\u672c\u5347\u7ea7',
                'verbose_name_plural': '\u7248\u672c\u5347\u7ea7',
            },
        ),
    ]
