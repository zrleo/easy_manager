# -*- coding:utf-8 -*-

import json
from django import forms


class AddProjectForm(forms.Form):
    project_name = forms.CharField(max_length=200)  # 项目名称

class ProjectListForm(forms.Form):
