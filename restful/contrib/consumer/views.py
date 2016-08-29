# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from restful.contrib.consumer.models import Contacts, History
from .serializers import (ProfileSerializer, AvatarSerializer, ContactsSerializer, HistorySerializer)
from .utils import get_user_profile


class ProfileViewSet(RetrieveUpdateAPIView):
    '''
    用户信息
    '''
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
    allowed_methods = ('GET', 'PUT', 'OPTIONS')

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     data = serializer.data
    #     # slug = self.request.user.slug.hex if self.request.user.slug else None
    #     # data['slug'] = short_url.encode_url(instance.pk)
    #     # data['qrcode'] = reverse('frontend.views.q', args=[data['slug']], request=request)
    #     return Response(data)

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


class ContactViewSet(viewsets.ModelViewSet):
    '''
    联系人接口.

    content 是读取手机联系人转成 `json` 提交到服务器
    结构如下:
    [
        {
            "name": "张三",
            "number": ["138991100122"]
        },
        {
            "name": "张三",
            "number": ["138991100122", "138991100122", "138991100122"]
        }
    ]


    '''
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = (IsAuthenticated,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_object(self):
        return self.get_queryset().filter(owner=self.request.user)


class HistoryViewSet(viewsets.ModelViewSet):
    '''
    通话历史接口.

    '''
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = (IsAuthenticated,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def get_object(self):
        return self.get_queryset().filter(owner=self.request.user)
