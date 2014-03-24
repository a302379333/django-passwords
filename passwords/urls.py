# coding: utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'password_validator/$', 'passwords.views.password_validator', name='password_validator'),
)
