# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from libs.models.mixins import TimeModelMixin
from libs.models.base import BaseModel
from .constants import METHOD, STATUS, TEST_RESULT


class Api(BaseModel, TimeModelMixin):
    '''
    接口
    '''
    project_id = models.CharField(u'项目ID', max_length=20)
    api_id = models.CharField(u'接口ID', max_length=20)
    api_name = models.CharField(u'接口名称', max_length=100, unique=True, null=False)
    api_url = models.URLField(u'接口URL', max_length=500)
    api_path = models.CharField(u'接口路径', max_length=500)
    request_method = models.CharField(u'请求方法', max_length=10, choices=METHOD.CHOICES, default=METHOD.POST)
    request_data = models.TextField(u'请求参数')
    response_data = models.TextField(u'实际响应结果')
    expect_response_data = models.TextField(u'期望结果')
    test_result = models.IntegerField(u'测试结果', choices=TEST_RESULT.CHOICES, default=TEST_RESULT.PASS)
    status = models.SmallIntegerField(u'接口状态', choices=STATUS.CHOICES, default=STATUS.NEW)

    class Meta:
        db_table = "api_api"
        unique_together = [['api_id']]
        index_together = [['created_time'], ['api_name']]

    def __unicode__(self):
        return self.api_name

    @property
    def brief_info(self):
        return {
            'project_id': self.project_id,
            'api_id': self.api_id,
            'api_name': self.api_name,
            'created_time': self.created_time.strftime('%Y-%m-%d %H:%M:%S'),
            'last_update': self.last_update.strftime('%Y-%m-%d %H:%M:%S'),
        }
