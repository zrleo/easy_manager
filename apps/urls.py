# -*- coding:utf-8 -*-

from django.conf.urls import url, include


urlpatterns = [
    url(r'^easy_manager/', include("apps.easy_api_manager_app.urls")),
    url(r'^users/', include("apps.users.urls")),

]


