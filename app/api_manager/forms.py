# -*- coding:utf-8 -*-

from django import forms
from .models import Api
from utils.errorcode import ERRORCODE


class ApiInfoForm(forms.Form):
    api_id = forms.CharField(max_length=100, required=True)
    api_name = forms.CharField(max_length=200, required=True)

    def clean_api_id(self):
        api_name = self.cleaned_data['api_name']
        if Api.objects.filter(api_name=api_name).exists():
            return forms.ValidationError('api name had used', ERRORCODE.HAD_USED)
        return api_name
