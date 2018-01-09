# -*- coding: utf-8 -*-
# !/usr/bin/env python

from libs.error.errorcode import CommonError, StatusCode


class ERRORCODE(CommonError):
    '''错误码
    '''
    BASE_CODE = 30000
    INVALID_PASSWORD = StatusCode(BASE_CODE + 1, 'invalid password', u'密码错误')
    HAD_USED = StatusCode(BASE_CODE + 2, 'had used', u'已经使用')
    INVALID_CODE = StatusCode(BASE_CODE + 3, 'invalid code', u'错误的短信验证码')
    INVALID_CAPTCHA = StatusCode(BASE_CODE + 4, 'invalid captcha', u'错误的验证码')
    SEND_VERIFICATION_OVER_RATE = StatusCode(BASE_CODE + 5, 'SEND_VERIFICATION_OVER_RATE', u'发送频率太高')
    NOT_AUDIT = StatusCode(BASE_CODE + 6, 'NOT AUDIT', u'尚未认证')
    NOT_REGISTER_MOBILE = StatusCode(BASE_CODE + 7, 'not register mobile', u'手机号码和注册号码不一致')
