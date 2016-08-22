# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

# from raven.contrib.django.raven_compat.middleware.wsgi import Sentry
# application = Sentry(application)
