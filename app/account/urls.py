# -*- coding:utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'registered/?', views.register_views, name='register_view'),
    url(r'login/?', views.login_views, name='login_view'),
    url(r'logout/?', views.logout_view, name='logout_view')
]
