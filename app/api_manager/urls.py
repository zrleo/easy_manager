# -*- coding:utf-8 -*-

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^add_api/?', views.add_api, name='add_api'),
    url(r'^api_list/?', views.api_list, name='api_list'),
    url(r'^api_edit/?', views.api_edit, name='api_edit'),
]
