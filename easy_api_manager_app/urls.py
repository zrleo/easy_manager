# -*- coding:utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login_action$', views.login_action_views, name='login'),
    url(r'^api_list_manager$', views.api_list_manager_views, name='api_manager'),
]