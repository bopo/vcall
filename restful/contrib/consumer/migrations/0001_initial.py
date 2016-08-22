# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import restful.contrib.consumer.models
import imagekit.models.fields
import model_utils.fields
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.UUIDField(verbose_name='slug', null=True, auto_created=True, blank=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mobile', models.CharField(db_index=True, max_length=25, verbose_name='\u624b\u673a\u53f7\u7801', blank=True)),
                ('verify_code', models.CharField(max_length=5, verbose_name='\u77ed\u4fe1\u7801', blank=True)),
                ('device', models.CharField(max_length=100, verbose_name='\u8bbe\u5907\u53f7')),
                ('jpush_registration_id', models.CharField(max_length=200, null=True, verbose_name='jpush_registration_id', blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', restful.contrib.consumer.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(default='', max_length=255, verbose_name='\u6536\u85cf\u5185\u5bb9\u7684\u6807\u9898')),
                ('mobile', models.CharField(default='', max_length=255, verbose_name='\u6536\u85cf\u5185\u5bb9\u7684\u63cf\u8ff0')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(default='', max_length=255, verbose_name='\u6536\u85cf\u5185\u5bb9\u7684\u6807\u9898')),
                ('url', models.CharField(default='', max_length=255, verbose_name='\u6536\u85cf\u5185\u5bb9\u7684\u539f\u6587\u5730\u5740\uff0c\u4e0d\u5e26\u57df\u540d')),
                ('summary', models.CharField(default='', max_length=255, verbose_name='\u6536\u85cf\u5185\u5bb9\u7684\u63cf\u8ff0')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='\u59d3\u540d', blank=True)),
                ('nick', models.CharField(db_index=True, max_length=255, null=True, verbose_name='\u6635\u79f0', blank=True)),
                ('phone', models.CharField(default='', max_length=64, verbose_name='\u7535\u8bdd', blank=True)),
                ('gender', models.CharField(default='male', max_length=10, verbose_name='\u6027\u522b', choices=[('male', '\u7537'), ('female', '\u5973')])),
                ('zodiac', models.CharField(max_length=25, verbose_name='\u661f\u5ea7', blank=True)),
                ('birthday', models.DateField(null=True, verbose_name='\u751f\u65e5', blank=True)),
                ('alipay', models.CharField(max_length=100, verbose_name='\u652f\u4ed8\u5b9d', blank=True)),
                ('qq', models.CharField(max_length=100, verbose_name='QQ', blank=True)),
                ('chinese_zodiac', models.CharField(max_length=25, verbose_name='\u751f\u8096', blank=True)),
                ('payment', models.DecimalField(default=0.0, verbose_name='\u5df2\u7ecf\u63d0\u73b0', max_digits=10, decimal_places=2)),
                ('balance', models.DecimalField(default=0.0, verbose_name='\u5e10\u6237\u4f59\u989d', max_digits=10, decimal_places=2)),
                ('total', models.DecimalField(default=0.0, verbose_name='\u5e10\u6237\u603b\u989d', max_digits=10, decimal_places=2)),
                ('qrcode', models.ImageField(upload_to='qrcode', verbose_name='\u4e8c\u7ef4\u7801')),
                ('avatar', imagekit.models.fields.ProcessedImageField(upload_to='avatar', null=True, verbose_name='\u5934\u50cf')),
                ('owner', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
    ]
