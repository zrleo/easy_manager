# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from libs.models import BaseModel, TimeModelMinxin
# Create your models here.


class ProjectModel(BaseModel, TimeModelMinxin):
    project_name = models.CharField(max_length=200, unique=True, )


