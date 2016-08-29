# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

import short_url
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.contenttypes import fields as generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ProcessedImageField
from model_utils.models import TimeStampedModel
from pilkit.processors import ResizeToFill
from rest_framework.serializers import ValidationError


class AbstractActionType(TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, blank=True, default=None)
    content_object = generic.GenericForeignKey('content_type', 'object_id', )

    def validate_unique(self):
        if (self.__class__.objects.filter(owner=self.owner, object_id=self.object_id,
                content_type=self.content_type).exists()):
            raise ValidationError({'detail': 'The record already exists. '})

    class Meta:
        abstract = True


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password,
            is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()

        if not username:
            raise ValueError('The given username must be set')

        # email = self.normalize_email(email)

        user = self.model(username=username,
            is_staff=is_staff, is_active=True,
            is_superuser=is_superuser,
            date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, True, True, **extra_fields)


class CustomUser(AbstractUser):
    """
    Concrete class of AbstractEmailUser.
    Use this if you don't need to extend EmailUser.
    """

    REQUIRED_FIELDS = []
    GENDER_CHOICES = (('male', '男'), ('female', '女'))
    name = models.CharField(_(u'用户姓名'), max_length=25, db_index=True, blank=True)
    mobile = models.CharField(_(u'手机号码'), max_length=25, db_index=True, blank=True)
    verify_code = models.CharField(_(u'短信码'), max_length=5, blank=True)
    device = models.CharField(_(u'设备号'), max_length=100, blank=False, null=False)
    slug = models.UUIDField(_(u'slug'), null=True, blank=True, auto_created=True)
    jpush_registration_id = models.CharField(_(u'jpush_registration_id'), max_length=200, blank=True, null=True)
    # birthday = models.DateField(_(u'生日'), blank=True, null=True)
    # zodiac_zh = models.CharField(_(u'生肖'), max_length=25, blank=True)
    # avatar = models.ImageField(_(u'头像'), max_length=200, blank=True)
    # zodiac = models.CharField(_(u'星座'), max_length=25, blank=True)
    # gender = models.CharField(_(u'性别'), max_length=25, default='male', choices=GENDER_CHOICES)
    # score_total = models.IntegerField(_(u'积分'), default=0)

    objects = CustomUserManager()

    def short(self):
        short_url.encode_url(self.pk)


class Message(TimeStampedModel):
    '''
    用户消息
    '''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    title = models.CharField(verbose_name=_(u'收藏内容的标题'), max_length=255, default='')
    url = models.CharField(verbose_name=_(u'收藏内容的原文地址，不带域名'), max_length=255, default='')
    summary = models.CharField(verbose_name=_(u'收藏内容的描述'), max_length=255, default='')


class Contacts(TimeStampedModel):
    '''
    联系人
    '''
    # STATIS = (('0', _('未注册')), ('1', _('注册')))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    content = models.TextField(_('联系人内容'), blank=True,null=True)
    # name = models.CharField(verbose_name=_(u'联系人姓名'), max_length=255, default='')
    # mobile = models.CharField(verbose_name=_(u'联系人手机'), max_length=255, default='')


class History(TimeStampedModel):
    '''
    通话记录
    '''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    name = models.CharField(verbose_name=_(u'联系人姓名'), max_length=255, default='')
    mobile = models.CharField(verbose_name=_(u'联系人手机'), max_length=255, default='')


class Verification(TimeStampedModel):
    mobile = models.CharField(verbose_name=_(u'手机号'), max_length=255, default='', unique=True)
    verify = models.CharField(verbose_name=_(u'验证码'), max_length=255, default='')

    # def check(self, verify):
    #     return self.verify == verify

    # def send(self):
    #     self.save()
    #     return self.verify

    class Meta:
        verbose_name = _("Verification")
        verbose_name_plural = _("Verification")

    def save(self, *args, **kwargs):
        if not self.verify:
            self.code = self.generate_key()
        return super(Verification, self).save(*args, **kwargs)

    def generate_key(self):
        return random.randint(100000, 999999)

    def __str__(self):
        return self.verify


class Profile(TimeStampedModel):
    '''
    该接口更新接受PUT方法

    性别字段英文对应汉字为:
    male:男
    female:女
    提交的数据要用英文.获取时候api也是英文, 要客户端自己做下转换.
    '''
    GENDER_CHOICES = (('male', '男'), ('female', '女'))
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, db_index=True, related_name='profile')
    name = models.CharField(verbose_name=_(u'姓名'), blank=True, max_length=255, db_index=True)
    nick = models.CharField(verbose_name=_(u'昵称'), blank=True, null=True, max_length=255, db_index=True)
    # phone = models.CharField(verbose_name=_(u'电话'), default='', blank=True, max_length=64)
    # gender = models.CharField(verbose_name=_(u'性别'), max_length=10, choices=GENDER_CHOICES, default=u'male')
    # zodiac = models.CharField(_(u'星座'), max_length=25, blank=True)
    # birthday = models.DateField(_(u'生日'), blank=True, null=True)
    # alipay = models.CharField(verbose_name=_(u'支付宝'), max_length=100, blank=True)
    # qq = models.CharField(verbose_name=_(u'QQ'), max_length=100, blank=True)
    # chinese_zodiac = models.CharField(_(u'生肖'), max_length=25, blank=True)
    #
    # payment = models.DecimalField(verbose_name=_(u'已经提现'), default=0.00, max_digits=10, decimal_places=2)
    # balance = models.DecimalField(verbose_name=_(u'帐户余额'), default=0.00, max_digits=10, decimal_places=2)
    # total = models.DecimalField(verbose_name=_(u'帐户总额'), default=0.00, max_digits=10, decimal_places=2)

    # qrcode = models.ImageField(verbose_name=_(u'二维码'), upload_to='qrcode')
    avatar = ProcessedImageField(verbose_name=_(u'头像'), upload_to='avatar', processors=[ResizeToFill(320, 320)],
        format='JPEG', null=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'profile')
        verbose_name_plural = _(u'profiles')
