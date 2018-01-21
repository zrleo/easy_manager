# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.db import transaction
from django.db import IntegrityError
from django.views.decorators.http import require_GET, require_POST
from libs.http.response import http_response
from libs.paginator.paginator import paginate_inc
from utils.errorcode import ERRORCODE
from .forms import AddProjectForm, ProjectListForm, ProjectDeleteForm
from .models import Project

# Create your views here.


@require_POST
def add_project_views(request):
    '''
    增加项目
    :param request:
    :return:
    '''
    form = AddProjectForm(request.POST)
    if not form.is_valid():
        json_msg = json.loads(form.errors.as_json())
        code = json_msg.values()[0][0]['code']
        return http_response(request, code=code if isinstance(code, int) else ERRORCODE.PARAM_ERROR.code, msg=json_msg)
    project_name = form.cleaned_data['project_name']
    project_id = form.cleaned_data['project_id']
    try:
        with transaction.atomic():
            project = Project.objects.create(
                project_name=project_name,
                project_id=project_id
            )
            project.save()
            response = http_response(request, statuscode=ERRORCODE.SUCCESS)
            return response
    except IntegrityError:
        return http_response(request, statuscode=ERRORCODE.HAD_USED)


@require_GET
def proj_list_views(request):
    '''
    项目列表
    :param request:
    :return:
    '''
    form = ProjectListForm(request.GET)
    if not form.is_valid():
        json_msg = json.loads(form.errors.as_json())
        code = json_msg.values()[0][0]['code']
        return http_response(request, code=code if isinstance(code, int) else ERRORCODE.PARAM_ERROR.code, msg=json_msg)
    project_qs = Project.objects.all().order_by('-created_time')
    page_obj, total = paginate_inc(project_qs,
                                   form.cleaned_data.get('page_num') or 1,
                                   form.cleaned_data.get('page_size') or 20)
    project_list = [project.brief_info for project in page_obj]
    context = {
        'total': total,
        'project_list': project_list
    }
    return http_response(request, context=context, statuscode=ERRORCODE.SUCCESS)


@require_POST
def project_edit_views(request):
    '''
    编辑项目信息
    :param request:
    :return:
    '''
    form = AddProjectForm(request.POST)
    if not form.is_valid():
        json_msg = json.loads(form.errors.as_json())
        code = json_msg.values()[0][0]['code']
        return http_response(request, code=code if isinstance(code, int) else ERRORCODE.PARAM_ERROR.code, msg=json_msg)
    project_id = request.POST.get('project_id')
    if not project_id:
        return http_response(request, statuscode=ERRORCODE.PARAM_ERROR, msg='product_id is required')
    #  TODO 这里有一个 bug, 当传过来的project_id不存在时，系统直接报错了，未处理异常
    try:
        project = Project.objects.get(project_id=project_id)
        project.project_name = form.cleaned_data['project_name']
        project.save()
        response = http_response(request, statuscode=ERRORCODE.SUCCESS)
        return response
    except Project.DoesNotExist:
        return http_response(request, statuscode=ERRORCODE.NOT_FOUND, msg=form.errors)


@require_POST
def delete_pro_views(request):
    '''
    删除项目
    :param request:
    :return:
    '''
    form = ProjectDeleteForm(request.POST)
    if not form.is_valid():
        json_msg = json.loads(form.errors.as_json())
        code = json_msg.values()[0][0]['code']
        return http_response(request, code=code if isinstance(code, int) else ERRORCODE.PARAM_ERROR.code, msg=json_msg)
    project_id = request.POST.get('project_id')
    if not project_id:
        return http_response(request, statuscode=ERRORCODE.PARAM_ERROR, msg='product_id is required')
    try:
        project = Project.objects.get(project_id=project_id)
        project.delete()
        response = http_response(request, statuscode=ERRORCODE.SUCCESS)
        return response
    except Project.DoesNotExist:
        return http_response(request, statuscode=ERRORCODE.NOT_FOUND, msg=form.errors)