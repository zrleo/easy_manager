# -*- coding:utf-8 -*-

import json
from django import forms
from libs.http.response import http_response
from .models import ProjectModel, ApiModel
from utils.errorcode import ERRORCODE


class AddProjectForm(forms.Form):
    project_name = forms.CharField(max_length=200)  # 项目名称

    def clean(self):
        project_name = self.cleaned_data['project_name']
        if ProjectModel.objects.filter(project_name=project_name).exists():
            return forms.ValidationError('project_name is invalid', ERRORCODE.HAD_USED)
        return project_name

