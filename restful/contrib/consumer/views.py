# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from jsonschema import validate
from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from restful.contrib.consumer.models import Contacts, History
from .serializers import (ProfileSerializer, AvatarSerializer, HistorySerializer,
    ContactPushSerializer, ContactsSerializer)
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


class ContactViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
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
    serializer_class = ContactPushSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ContactsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        schema = {
            "type": "array",
            "items": {
                'type': 'object',
                'properties': {
                    "number": {"type": "array"},
                    "name": {"type": "string"},
                },
            },
        }

        # try:
        content = request.data.get('content')
        content = json.loads(content)
        # 校验格式
        validate(content, schema)

        # 写入数据库
        for item in content:
            for mobile in item.get('number'):
                print mobile
                # if mobile and re.match(r'^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$', mobile):

                if mobile:
                    contact, status_ = Contacts.objects.get_or_create(mobile=mobile)

                    if status_:
                        content.name = item.get('name')
                        content.save()

        queryset = self.filter_queryset(self.get_queryset())
        serializer = ContactsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        # return Contacts.objects.filter(owner=self.request.user)
        return Contacts.objects.all()


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
