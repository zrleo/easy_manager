# -*- coding:utf-8 -*-

from django import forms
from .models import Project, Api
from utils.errorcode import ERRORCODE


class AddProjectForm(forms.Form):
    project_id = forms.CharField(max_length=20)
    project_name = forms.CharField(max_length=200)  # 项目名称

    def clean_pro_name(self):
        project_name = self.cleaned_data['project_name']
        if Project.objects.filter(project_name=project_name).exists():
            return forms.ValidationError('project_name is invalid', ERRORCODE.HAD_USED)
        return project_name


class ProjectListForm(forms.Form):
    project_name = forms.CharField(max_length=200, required=False)
