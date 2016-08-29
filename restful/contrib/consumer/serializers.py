# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from .models import Profile, Contacts, History


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = get_user_model()
        # fields = ('id', 'username', 'name', 'email', 'phone', 'groups', 'is_active')


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("avatar",)


class AvatarRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.url


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("name", "nick", "avatar")


class PasswordSerializer(serializers.Serializer):
    pass


class ContactPushSerializer(serializers.Serializer):
    content = serializers.CharField(required=True, allow_blank=True, label=_(u'提交的json'), trim_whitespace=True)


class ContactsSerializer(serializers.ModelSerializer):
    # def validate(self, attrs):
    #     pass

    class Meta:
        model = Contacts
        fields = ("name", "mobile", "status")


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ("name", "mobile", "modified")
