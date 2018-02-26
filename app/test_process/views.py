# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from ..api_manager.models import Api
# Create your views here.


def get_param(request, api_id):
    '''
    查询数据库获得参数
    :return:
    '''
    api_url, api_path, request_data, request_method = Api.objects.filter(api_id=api_id)
