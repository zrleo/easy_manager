# -*- coding:utf-8 -*-

import datetime
from django.db import models


class BaseModel(models.Model):
    create_time = models.TimeField(datetime.datetime.now())
    update_time = models.TimeField(datetime.datetime.now())


class TimeModelMinxin(models.Model):
    pass