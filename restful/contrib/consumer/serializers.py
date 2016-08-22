# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import Profile, Contacts


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    # groups = GroupSerializer(many=True)
    # phone = serializers.CharField(source='profile.phone', read_only=True)
    # name = serializers.CharField(source='profile.name', read_only=True)

    # menus = serializers.SerializerMethodField()
    # is_active = serializers.BooleanField(source='profile.is_cms_active')

    # def get_menus(self, user):
    #     return get_menus(user)

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
    qrcode = serializers.URLField(read_only=True)
    jpush_registration_id = serializers.CharField(source='owner.jpush_registration_id', read_only=True)

    class Meta:
        model = Profile
        read_only_fields = ("payment", "balance", "total",)
        fields = ("name", "nick", "phone", "avatar", "gender", "zodiac", "birthday", "alipay", "qq",
        "payment", "balance", "total", "qrcode", "jpush_registration_id")


class PasswordSerializer(serializers.Serializer):
    pass


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ("name", "mobile",)
