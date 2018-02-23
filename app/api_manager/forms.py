# -*- coding:utf-8 -*-

from django import forms
from .models import Api
from utils.errorcode import ERRORCODE
from .constants import METHOD, STATUS


class ApiInfoForm(forms.Form):
    project_id = forms.CharField(max_length=20)
    project_name = forms.CharField(max_length=200)
    api_id = forms.CharField(max_length=20)
    api_name = forms.CharField(max_length=100)
    api_url = forms.URLField(max_length=500)
    api_path = forms.CharField(max_length=500)
    request_method = forms.IntegerField()
    request_data = forms.CharField()
    expect_response_data = forms.CharField()

    def clean_api_name(self):
        api_name = self.cleaned_data['api_name']
        if Api.objects.filter(api_name=api_name).exists():
            return forms.ValidationError('api name had used', ERRORCODE.HAD_USED)
        return api_name


    # class Meta:
    #     model = Api
    #     fields = ['api_name', 'project_id', 'api_id', 'api_path', 'api_url',
    #               'request_data', 'request_method', 'expect_response_data', 'status']


class ApiListForm(forms.Form):
    api_name = forms.CharField(max_length=100, required=False)


# class ApiEditForm(forms.Form):
#     api_name = forms.CharField()
#     api_url = forms.URLField()
#     api_path = forms.CharField(max_length=500)
#     request_method = forms.IntegerField()
#     request_data = forms.Textarea()
#     expect_response_data = forms.Textarea()
