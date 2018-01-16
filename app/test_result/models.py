# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .constants import TEST_RESULT
from libs.models.mixins import TimeModelMixin
# Create your models here.


class Result(TimeModelMixin):
    """
    测试结果
    """
    api_id = models.CharField(u'接口ID', max_length=20)
    result_id = models.CharField(u'结果ID', max_length=20)
    result_name = models.CharField(u'测试结果名称', max_length=100)
    response_data = models.TextField(u'实际响应结果')
    test_result = models.IntegerField(u'测试结果', choices=TEST_RESULT.CHOICES, default=TEST_RESULT.PASS)

    class Meta:
        db_table = "result_result"
        unique_together = [['result_id']]
        index_together = [['created_time'], ['result_name']]

    def __str__(self):
        return self.result_name
