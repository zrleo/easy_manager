# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.db import transaction, IntegrityError


from .forms import RegisteredForm
from libs.http.response import http_response
from utils.errorcode import ERRORCODE
from .models import Account
from .backend import update_userinfo_session_cookie
# Create your views here.


def register_views(request):
    '''
    注册接口
    :param request:
    :return:
    '''
    form = RegisteredForm(request.POST)
    if not form.is_valid():
        json_msg = json.loads(form.errors.as_json())
        code = json_msg.values()[0][0]['code']
        return http_response(request, code=code if isinstance(code, int) else ERRORCODE.PARAM_ERROR.code, msg=json_msg)

    email = form.cleaned_data['email']
    name_cn = form.cleaned_data['name_cn']
    department = form.cleaned_data['department']
    password = form.cleaned_data['password']

    try:
        with transaction.atomic():
            account = Account.objects.create(
                email=email,
                name_cn=name_cn,
                deparment=department
            )
            account.set_password(password)
            account.save()
            # 登录

            response = http_response(request, statuscode=ERRORCODE.SUCCESS)
            update_userinfo_session_cookie(request, response, account)
            return response
    except IntegrityError:
        return http_response(request, statuscode=ERRORCODE.HAD_USED)