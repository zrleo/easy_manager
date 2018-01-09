# -*- coding:utf-8 -*-
from django import forms
from libs.forms.validators import email_validator
from app.account.models import User
from sdks.securecode.verifycode import MobileCode
from sdks.securecode.constants import MobileVerifyKind
from app.account.models import Account
from app.account.constants import CaptchaType
from utils.errorcode import ERRORCODE


class RegisteredForm(forms.Form):
    '''
    注册form
    '''
    email = forms.CharField(max_length=30, validators=[email_validator])
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32, min_length=8)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email had used', code=ERRORCODE.HAD_USED.code)
        return email

    def clean(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('PARAM ERROR', code=ERRORCODE.PARAM_ERROR.code)


class LoginForm(forms.Form):
    mobile = forms.CharField(max_length=11, validators=[mobile_validator])
    password = forms.CharField(max_length=32, min_length=8)
    captcha = forms.CharField(max_length=4, validators=[captcha_validator])
    captcha_key = forms.CharField(max_length=64)

    def clean(self):
        captcha = self.cleaned_data.get('captcha')
        captcha_key = self.cleaned_data.get('captcha_key')

        if not (captcha and captcha_key):
            raise forms.ValidationError('invalid captcha', code=ERRORCODE.PARAM_ERROR.code)

        ret, _ = Captcha.verify_captcha(captcha_key, captcha, kind=CaptchaType.Login)
        if ret:
            return self.cleaned_data
        else:
            raise forms.ValidationError('invalid captcha', code=ERRORCODE.INVALID_CAPTCHA.code)


class ReplaceMobileForm(forms.Form):
    mobile = forms.CharField(max_length=11, validators=[mobile_validator])
    code = forms.CharField(max_length=6, validators=[verify_code_validator])
    token = forms.CharField(max_length=32, min_length=32, required=False)

    def clean(self):
        mobile = self.cleaned_data.get('mobile')
        code = self.cleaned_data.get('code')
        token = self.cleaned_data.get('token')

        if not (mobile and code):
            raise forms.ValidationError('invalid phone code', code=ERRORCODE.INVALID_CODE.code)
        if token:
            # 第二次验证
            kind = MobileVerifyKind.CHANGE_MOBILE_VERIFY
        else:
            kind = MobileVerifyKind.CHANGE_MOBILE
        code = MobileCode.verify_mobile_code(
            kind=kind,
            mobile=mobile,
            code=code,
        )
        if code != ERRORCODE.SUCCESS.code:
            raise forms.ValidationError('invalid phone code', code=ERRORCODE.INVALID_CODE.code)
        return self.cleaned_data


class FindPasswdForm(forms.Form):
    mobile = forms.CharField(max_length=11, validators=[mobile_validator])
    code = forms.CharField(max_length=6, validators=[verify_code_validator])
    password = forms.CharField(max_length=32, min_length=8)

    def clean(self):
        mobile = self.cleaned_data.get('mobile')
        verifycode = self.cleaned_data.get('code')

        if not (mobile and verifycode):
            raise forms.ValidationError('invalid phone code', code=ERRORCODE.INVALID_CODE.code)

        code = MobileCode.verify_mobile_code(
            kind=MobileVerifyKind.FIND_PASSWD,
            mobile=mobile,
            code=verifycode
        )
        if code != ERRORCODE.SUCCESS.code:
            raise forms.ValidationError('invalid phone code', code=ERRORCODE.INVALID_CODE.code)
        return self.cleaned_data


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(max_length=32)
    new_password = forms.CharField(max_length=32, min_length=8)
