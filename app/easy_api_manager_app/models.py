# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from libs.models.mixins import TimeModelMixin, EditorModelMixin
from libs.models.base import BaseModel


# Create your models here.


class ProjectModel(BaseModel, TimeModelMixin):
    project_name = models.CharField(max_length=200, unique=True, )


