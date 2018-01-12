# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from libs.models.mixins import TimeModelMixin, EditorModelMixin
from libs.models.base import BaseModel
from .constants import METHOD, STATUS

# Create your models here.


class Project(BaseModel, TimeModelMixin):
    project_name = models.CharField(u'项目名称', max_length=200, unique=True)

    class Meta:
        db_table = "project_project"


class Api(BaseModel, TimeModelMixin):
    api_name = models.CharField(u'接口名称', max_length=100, unique=True, null=False)
    api_url = models.URLField(u'接口URL', max_length=500)
    api_path = models.CharField(u'接口路径', max_length=500)
    request_method = models.CharField(u'请求方法', max_length=10, choices=METHOD.CHOICES, default=METHOD.POST)
    request_date = models.TextField(u'请求参数')
    response_data = models.TextField(u'响应参数')
    status = models.SmallIntegerField(u'接口状态', choices=STATUS.CHOICES, default=STATUS.WAIT)

    class Meta:
        db_table = "api_api"

    def __str__(self):
        return self.api_name

