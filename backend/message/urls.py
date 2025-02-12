#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Python imports.

# Django imports.
from django.urls import path

from message.views import MessageApiView


app_name = 'message'

urlpatterns = [
    path('', MessageApiView.as_view(), name='message-api'),
]
