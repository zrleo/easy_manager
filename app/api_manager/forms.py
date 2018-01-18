# -*- coding:utf-8 -*-

from django import forms
from .models import Api
from utils.errorcode import ERRORCODE


class ApiInfoForm(forms.ModelForm):
    class Meta:
        model = Api
        fields = ['api_name', 'project_id', 'api_id', 'api_path', 'api_url',
                  'request_data', 'request_method', 'expect_response_data', 'status']

    def clean_api_name(self):
        api_name = self.cleaned_data['api_name']
        if Api.objects.filter(api_name=api_name).exists():
            print "++++++++"
            return forms.ValidationError('api name had used', ERRORCODE.HAD_USED)
        return api_name
