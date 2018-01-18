# -*- coding:utf-8 -*-

from django.conf.urls import url, include


urlpatterns = [
    url(r'^project_manager/', include("app.easy_api_manager_app.urls")),
    url(r'^account_manager/', include("app.account.urls")),
    url(r'^api_manager/', include("app.api_manager.urls")),
]


