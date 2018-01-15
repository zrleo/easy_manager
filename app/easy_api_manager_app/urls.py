# -*- coding:utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add_project/?', views.add_project_views, name='add_project_views'),
    url(r'^project_list/?', views.proj_list_views, name='proj_list_views'),
    url(r'^project_edit/?', views.project_edit_views, name='project_edit_views'),
    url(r'^delete_project/?', views.delete_pro_views, name='delete_pro_views'),
]
