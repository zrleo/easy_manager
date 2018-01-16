# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import render
from django.db import transaction
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
    api_id = forms.cleaned_data['api_id']
    api_name = forms.cleaned_data['api_name']
    try:
        with transaction.atomic():
            api = ApiInfoForm.objects.create(
                api_id=api_id,
                api_name=api_name,
                api_url=api_url,
                project_name=project_name,
                project_id=project_id
            )
            project.save()
            response = http_response(request, statuscode=ERRORCODE.SUCCESS)
            return response
    except IntegrityError:
        return http_response(request, statuscode=ERRORCODE.HAD_USED)