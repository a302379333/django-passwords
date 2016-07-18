# coding: utf-8
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from django.conf.urls import  url

from .views import password_validator

urlpatterns = [
    url(r'password_validator/$', password_validator, name='password_validator'),
]
