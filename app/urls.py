# -*- coding:utf-8 -*-

from django.conf.urls import url, include


urlpatterns = [
    url(r'^easy_manager/', include("app.easy_api_manager_app.urls")),
    url(r'^account/', include("app.account.urls")),

]


