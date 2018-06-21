from __future__ import absolute_import, unicode_literals, division

from django.conf.urls import url
from django.urls import path

from .api import LockAPIView

__all__ = ('urlpatterns', )

urlpatterns = [
    path('api/lock/<app>/<model>/', LockAPIView.as_view(), name='locking-api'),

    path('api/lock/<app>/<model>/<int:object_id>/', LockAPIView.as_view(), name='locking-api'),
]
