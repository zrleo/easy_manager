# -*- coding: utf-8 -*-

import json
from __future__ import unicode_literals
from ..api_manager.models import Api
from forms import runTestForm
from libs.http.response import http_response
from utils.errorcode import ERRORCODE
from .bankend import run_test_single


def get_param(request):
    '''
    查询数据库获得参数
    :return:
    '''
    forms = runTestForm(request.GET)
    if not forms.is_valid():
        json_msg = json.loads(forms.errors.as_json())
        code = json_msg.values()[0][0]['code']
        return http_response(request, code=code if isinstance(code, int) else ERRORCODE.PARAM_ERROR.code, msg=json_msg)

    api_id = forms.cleaned_data['api_id']
    if not api_id:
        return http_response(request, statuscode=ERRORCODE.PARAM_ERROR, msg='api_id is required')
    try:
        api_qs = Api.objects.get(api_id=api_id)
        api_info = api_qs.brief_info
        api_path = api_info.get('api_path', '')
        api_url = api_info.get('api_url', '')
        request_data = api_info.get('request_data', '')
        request_method = api_info.get('request_method', '')
        expect_response_data = api_info.get('expect_response_data', '')
        run_test_single(api_path, api_url, request_data, request_method, expect_response_data)
        return http_response(request, )

    except Api.DoesNotExist:
        return http_response(request, statuscode=ERRORCODE.NOT_FOUND, msg=forms.errors)

