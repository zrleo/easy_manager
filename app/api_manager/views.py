# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.db import transaction
from django.db import IntegrityError
from .forms import ApiInfoForm
from libs.http.response import http_response
from utils.errorcode import ERRORCODE
from .models import Api


def add_api(request):
    '''
    添加api
    :param request:
    :return:
    '''
    forms = ApiInfoForm(request.POST)
    if not forms.is_valid():
        json_msg = json.loads(forms.errors.as_json())
        code = json_msg.values()[0][0]['code']
        return http_response(request, code=code if isinstance(code, int) else ERRORCODE.PARAM_ERROR.code, msg=json_msg)
    project_id = forms.cleaned_data['project_id']
    api_id = forms.cleaned_data['api_id']
    api_name = forms.cleaned_data['api_name']
    api_url = forms.cleaned_data['api_url']
    api_path = forms.cleaned_data['api_path']

    try:
        with transaction.atomic():
            api = Api.objects.create(
                api_id=api_id,
                api_name=api_name,
                api_url=api_url,

            )
            api.save()
            response = http_response(request, statuscode=ERRORCODE.SUCCESS)
            return response
    except IntegrityError:
        print "______"
        return http_response(request, statuscode=ERRORCODE.HAD_USED)
