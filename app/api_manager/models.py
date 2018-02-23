# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from libs.models.mixins import TimeModelMixin
from libs.models.base import BaseModel
from .constants import METHOD, STATUS


class Api(BaseModel, TimeModelMixin):
    '''
    接口
    '''
    project_id = models.CharField(u'项目ID', max_length=20, default=1)
    project_name = models.CharField(u'项目名称', max_length=200)
    api_id = models.CharField(u'接口ID', max_length=20)
    api_name = models.CharField(u'接口名称', max_length=100, unique=False)
    api_url = models.URLField(u'接口URL', max_length=500)
    api_path = models.CharField(u'接口路径', max_length=500)
    request_method = models.IntegerField(u'请求方法', choices=METHOD.CHOICES, default=METHOD.POST)
    request_data = models.CharField(u'请求参数', max_length=2048)
    expect_response_data = models.CharField(u'期望结果', default=None, max_length=2048)

    class Meta:
        db_table = "api_api"
        unique_together = [['api_id']]
        index_together = [['created_time'], ['api_name']]

    def __unicode__(self):
        return self.api_name

    @property
    def brief_info(self):
        return {
            'project_name': self.project_name,
            'api_id': self.api_id,
            'api_name': self.api_name,
            'created_time': self.created_time.strftime('%Y-%m-%d %H:%M:%S'),
            'last_update': self.last_update.strftime('%Y-%m-%d %H:%M:%S'),
        }
