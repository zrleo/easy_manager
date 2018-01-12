# -*- coding:utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add_project/?', views.add_project_views, name='add_project_views')
]
