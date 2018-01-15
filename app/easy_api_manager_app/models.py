# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from libs.models.base import BaseModel
from libs.models.mixins import TimeModelMixin, EditorModelMixin


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
