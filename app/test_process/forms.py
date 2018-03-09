# -*- coding:utf-8 -*-

from django import forms


class runTestForm(forms.Form):
    api_id = forms.CharField(max_length=100, required=True)
