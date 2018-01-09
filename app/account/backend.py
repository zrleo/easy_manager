# -*- coding:utf-8 -*-

import json
from django.conf import settings

from .constants import USERINFO_COOKIE_KEY


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