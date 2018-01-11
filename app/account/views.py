# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.db import transaction, IntegrityError
from django.contrib.auth import logout, authenticate
from .forms import RegisteredForm, LoginForm
from libs.http.response import http_response
from utils.errorcode import ERRORCODE
from .models import Account
from .backend import update_userinfo_session_cookie, do_login
from .constants import USERINFO_COOKIE_KEY
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
    password = form.cleaned_data['password']
    department = form.cleaned_data['department']

    try:
        with transaction.atomic():
            account = Account.objects.create(
                email=email,
                name_cn=name_cn,
                department=department,
            )
            account.set_password(password)
            account.save()
            do_login(request, account)
            response = http_response(request, statuscode=ERRORCODE.SUCCESS)
            update_userinfo_session_cookie(request, response, account)
            return response
    except IntegrityError:
        return http_response(request, statuscode=ERRORCODE.HAD_USED)


def login_views(request):
    '''
    登录接口
    :param request:
    :return:
    '''
    form = LoginForm(request.POST)
    if not form.is_valid():
        json_msg = json.loads(form.errors.as_json())
        code = json_msg.values()[0][0]['code']
        return http_response(request, code=code if isinstance(code, int) else ERRORCODE.PARAM_ERROR.code, msg=json_msg)

    email = form.cleaned_data['email']
    password = form.cleaned_data['password']
    if not Account.objects.filter(email=email).exists():
        return http_response(request, statuscode=ERRORCODE.NOT_FOUND)
    if request.user.is_authenticated():
        logout(request)

    user = authenticate(username=email, password=password)
    if not user:
        return http_response(request, statuscode=ERRORCODE.INVALID_PASSWORD)
    if not user.is_active:
        return http_response(request, statuscode=ERRORCODE.IN_BLACKLIST)
    do_login(request, user)

    response = http_response(request, statuscode=ERRORCODE.SUCCESS)
    update_userinfo_session_cookie(request, response, user)
    return response


def logout_view(request):
    '''
    退出接口
    :param request:
    :return:
    '''
    logout(request)
    response = http_response(request, statuscode=ERRORCODE.SUCCESS)
    # 删除 cookies
    response.delete_cookie(
        USERINFO_COOKIE_KEY,
    )
    return response

