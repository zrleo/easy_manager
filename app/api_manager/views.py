# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import render
from .forms import ApiInfoForm
from libs.http.response import http_response
from utils.errorcode import ERRORCODE


def add_api(request):
    '''
    添加api
    :param request:
    :return:
    '''
    forms = ApiInfoForm(request.POST)
    if not forms.is_valid():
        json_msg = json.loads(forms.as_json())
        code = json_msg.values()[0][0]['code']
        return http_response(request, code=code if isinstance(code, int)else ERRORCODE.PARAM_ERROR, msg=json_msg)