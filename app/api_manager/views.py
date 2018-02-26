# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.db import transaction
from django.db import IntegrityError
from django.views.decorators.http import require_GET, require_POST

from .forms import ApiInfoForm, ApiListForm
from libs.http.response import http_response
from libs.paginator.paginator import paginate_inc
from utils.errorcode import ERRORCODE
from .models import Api
from . import constants
from .backend import get_project


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
    project_name = forms.cleaned_data['project_name']
    api_id = forms.cleaned_data['api_id']
    api_name = forms.cleaned_data['api_name']
    api_url = forms.cleaned_data['api_url']
    api_path = forms.cleaned_data['api_path']
    request_data = forms.cleaned_data['request_data']
    request_method = forms.cleaned_data['request_method']
    expect_response_data = forms.cleaned_data['expect_response_data']
    try:
        with transaction.atomic():
            api = Api.objects.create(
                project_id=project_id,
                api_id=api_id,
                api_name=api_name,
                api_url=api_url,
                project_name=project_name,
                api_path=api_path,
                request_data=request_data,
                request_method=request_method,
                expect_response_data=expect_response_data,
            )
            api.save()
            response = http_response(request, statuscode=ERRORCODE.SUCCESS)
            return response
    except IntegrityError:
        return http_response(request, statuscode=ERRORCODE.HAD_USED)


@require_GET
def api_list(request):
    '''
    接口列表
    :param request:
    :return:
    '''
    form = ApiListForm(request.GET)
    if not form.is_valid():
        json_msg = json.loads(form.errors.as_json())
        code = json_msg.values()[0][0]['code']
        return http_response(request, code=code if isinstance(code, int) else ERRORCODE.PARAM_ERROR.code, msg=json_msg)
    api_qs = Api.objects.filter().all()
    page_obj, total = paginate_inc(api_qs, form.cleaned_data.get('page_num') or 1,
                                   form.cleaned_data.get('page_size') or 20)
    api_list = [api.brief_info for api in page_obj]
    context = {
        'total': total,
        'api_list': api_list
    }
    return http_response(request, context=context, statuscode=ERRORCODE.SUCCESS)


@require_POST
def api_edit(request):
    '''
    修改接口信息
    :param request:
    :return:
    '''
    form = ApiInfoForm(request.POST)
    if not form.is_valid():
        json_msg = json.loads(form.errors.as_json())
        code = json_msg.values()[0][0]['code']
        return http_response(request, code=code if isinstance(code, int) else ERRORCODE.PARAM_ERROR.code, msg=json_msg)
    api_id = request.POST.get('api_id')
    if not api_id:
        return http_response(request, statuscode=ERRORCODE.PARAM_ERROR, msg='api_id is required')
    try:
        api = Api.objects.get(api_id=api_id)
        print api.api_name
    except Api.DoesNotExist:
        return http_response(request, statuscode=ERRORCODE.NOT_FOUND, msg='api does not exist')
    name = form.cleaned_data['api_name']
    if name[0] == u'api name had used':
        api.api_name = api.api_name
    else:
        api.api_name = name
    api.api_url = form.cleaned_data['api_url']
    api.api_path = form.cleaned_data['api_path']
    api.request_data = form.cleaned_data['request_data']
    api.request_method = form.cleaned_data['request_method']
    api.expect_response_data = form.cleaned_data['expect_response_data']
    api.save()
    response = http_response(request, statuscode=ERRORCODE.SUCCESS)
    return response
