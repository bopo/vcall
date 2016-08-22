# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import INSTALLED_APPS

INSTALLED_APPS += (
    'restful',
    'restful.contrib.runner',
    'restful.contrib.consumer',
    'restful.contrib.restauth',
    'restful.contrib.restauth.registration',

    'imagekit',
    'easy_select2',
    'import_export',
    'reversion',
    # 'django_mobile',
    # 'rest_framework_swagger',
)

APPEND_SLASH = True
DEVICE_MAX_REG_NUMS = 5
