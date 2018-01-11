# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from libs.models.mixins import TimeModelMixin, EditorModelMixin
from libs.models.base import BaseModel


# Create your models here.


class ProjectModel(BaseModel, TimeModelMixin):
    project_name = models.CharField(u'项目名称', max_length=200, unique=True)

    class Meta:
        db_table = "project_project"


class ApiModel(BaseModel, TimeModelMixin):
    api_name = models.CharField(u'接口名称', max_length=100, unique=True, null=False)
    api_url = models.CharField(u'接口URL')