# -*- coding:utf-8 -*-

import json
from importlib import import_module
from django.conf import settings
from django.contrib.auth import login
from .constants import USERINFO_COOKIE_KEY
from .models import UserSessionKey

def get_user_info(user):
    # 获取用户信息 id， username
    return {
        'user_id': user.id,
        'user_name': user.name_cn,
    }


def update_userinfo_session_cookie(request, response, user):
    '''更新并延长userinfo的session和cookie，用户userinfo信息变更之后必须调用此方法'''
    user_info = get_user_info(user)
    # 更新session
    request.session['user_info'] = user_info
    request.session.set_expiry(settings.SESSION_COOKIE_AGE)
    request.session.save()
    # 设置cookie
    response.set_cookie(
        USERINFO_COOKIE_KEY,
        json.dumps(user_info),
        expires=settings.SESSION_COOKIE_AGE,
    )


def kickout_pre_session(request):
    '''更新session，剔除之前的登录session，记录当前的session'''
    user_id = request.user.id
    now_session_key = request.session.session_key
    try:
        pre_session = UserSessionKey.objects.get(user_id=user_id)
        pre_session_key = pre_session.session_key
    except UserSessionKey.DoesNotExist:
        # 之前没有可用登录状态
        pre_session_key = None

    if pre_session_key and now_session_key != pre_session_key:
        # delete pre session_key
        engine = import_module(settings.SESSION_ENGINE)
        s = engine.SessionStore(session_key=pre_session_key)
        s.delete()
        # update new UserSessionKey
        pre_session.session_key = now_session_key
        pre_session.save()
    elif not pre_session_key:
        UserSessionKey.objects.create(user_id=user_id, session_key=now_session_key)


def do_login(request, user):
    user.backend = settings.AUTHENTICATION_BACKENDS[0]
    login(request, user)
    kickout_pre_session(request)
