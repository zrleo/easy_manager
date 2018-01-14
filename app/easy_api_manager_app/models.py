# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from libs.models.mixins import TimeModelMixin, EditorModelMixin
from libs.models.base import BaseModel
from .constants import METHOD, STATUS

# Create your models here.


class Project(BaseModel, TimeModelMixin):
    '''
    项目
    '''
    project_id = models.CharField(u'项目编号', max_length=20)
    project_name = models.CharField(u'项目名称', max_length=200, unique=False)

    class Meta:
        db_table = "project_project"
        unique_together = [['project_id']]
        index_together = [['created_time'], ['project_name']]  # 添加索引

    def __unicode__(self):
        return self.project_name

    @property
    def breif_info(self):
        return {
            'project_id': self.project_id,
            'project_name': self.project_name,
            'created_time': self.created_time.strftime('%Y-%m-%d %H:%M:%S'),
            'last_update': self.last_update.strftime('%Y-%m-%d %H:%M:%S'),
        }


class Api(BaseModel, TimeModelMixin):
    '''
    接口
    '''
    api_id = models.CharField(u'接口ID', max_length=20)
    api_name = models.CharField(u'接口名称', max_length=100, unique=True, null=False)
    api_url = models.URLField(u'接口URL', max_length=500)
    api_path = models.CharField(u'接口路径', max_length=500)
    request_method = models.CharField(u'请求方法', max_length=10, choices=METHOD.CHOICES, default=METHOD.POST)
    request_date = models.TextField(u'请求参数')
    response_data = models.TextField(u'响应参数')
    status = models.SmallIntegerField(u'接口状态', choices=STATUS.CHOICES, default=STATUS.WAIT)

    class Meta:
        db_table = "api_api"
        unique_together = [['api_id']]
        index_together = [['created_time'], ['api_name']]

    def __unicode__(self):
        return self.api_name

    @property
    def breif_info(self):
        return {
            'api_id': self.api_id,
            'api_name': self.api_name,
            'created_time': self.created_time.strftime('%Y-%m-%d %H:%M:%S'),
            'last_update': self.last_update.strftime('%Y-%m-%d %H:%M:%S'),
        }
