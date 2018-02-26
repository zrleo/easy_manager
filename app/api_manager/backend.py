# -*- coding:utf-8 -*-

import json

from ..easy_api_manager_app.models import Project


def get_project(project_id):
    '''
    根据project_id 获取对应的project_name
    :param project_id:
    :return:
    '''
    project_name_set = Project.objects.filter(project_id=project_id)
    if project_name_set:
        project_name = str(project_name_set[0])
        return project_name
    return []


def get_method(request_method):
    '''

    :param request_method:
    :return:
    '''
