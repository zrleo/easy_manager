# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import AddProjectForm

# Create your views here.

# 首页(登录)


def add_project_views(request):
    form = AddProjectForm(request.POST)
    if



def index(request):
    return render(request, "index.html")


# 登录动作
def login_action_views(request):
    if request.method == "POST":
        # 寻找名为 "username"和"password"的POST参数，而且如果参数没有提交，返回一个空的字符串。
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == '' or password == '':
            return render(request, "index.html", {"error": "username or password null!"})

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 验证登录
            print user
            response = HttpResponseRedirect('api_list_manager')  # 登录成功跳转到接口列表页
            request.session['username'] = username    # 将 session 信息写到服务器
            return response
        else:
            return render(request, "index.html", {"error": "username or password error!"})
    # 防止直接通过浏览器访问 /login_action/ 地址。
    return render(request, "index.html")


# 登出
@login_required()
def logout_action_views(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')


@login_required()
def api_list_manager_views(request):
    return render(request, "api_list.html")


