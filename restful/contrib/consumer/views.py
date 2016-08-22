# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import short_url
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

from restful.contrib.consumer.models import Contacts
from .serializers import (ProfileSerializer, AvatarSerializer, ContactsSerializer)
from .utils import get_user_profile


class ProfileViewSet(RetrieveUpdateAPIView):
    '''
    用户信息
    '''
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
    allowed_methods = ('GET', 'PUT', 'OPTIONS')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        # slug = self.request.user.slug.hex if self.request.user.slug else None
        data['slug'] = short_url.encode_url(instance.pk)
        data['qrcode'] = reverse('frontend.views.q', args=[data['slug']], request=request)
        return Response(data)

    def get_object(self):
        return get_user_profile(self.request.user)


class AvatarViewSet(RetrieveUpdateAPIView):
    '''
    头像上传接口.

    '''
    serializer_class = AvatarSerializer
    permission_classes = (IsAuthenticated,)
    allowed_methods = ('PUT', 'OPTIONS')

    def get_object(self):
        return get_user_profile(self.request.user)


class ContactsViewSet(viewsets.ModelViewSet):
    '''
    联系人接口.

    '''
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = (IsAuthenticated,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def get_object(self):
        return self.get_queryset().filter(owner=self.request.user)
