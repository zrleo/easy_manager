# -*- coding:utf-8 -*-
from django import forms
from libs.forms.validators import email_validator
from app.account.models import Account
from utils.errorcode import ERRORCODE


class RegisteredForm(forms.Form):
    '''
    注册form
    '''
    email = forms.CharField(max_length=30, validators=[email_validator])
    name_cn = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32, min_length=8)
    department = forms.CharField(max_length=100)

    def clean_email(self):
        email = self.cleaned_data['email']
        if Account.objects.filter(email=email).exists():
            raise forms.ValidationError('email had used', code=ERRORCODE.HAD_USED.code)
        return email

    def clean(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('PARAM ERROR', code=ERRORCODE.PARAM_ERROR.code)


class LoginForm(forms.Form):
    '''
    登录form
    '''
    email = forms.CharField(max_length=100, validators=[email_validator])
    password = forms.CharField(max_length=32, min_length=8)

