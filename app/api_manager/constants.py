# -*- coding:utf-8 -*-


class METHOD(object):
    '''requests 请求方法'''
    POST = 0
    GET = 1
    PUT = 2
    DELETE = 10
    HEAD = 11
    CONNECT = 20
    OPTIONS = 30
    TRACE = 40

    CHOICES = (
        (GET, 'GET方法'),
        (POST, 'POST方法'),
        (PUT, 'PUT方法'),
        (DELETE, 'DELETE方法'),
        (HEAD, 'HEAD方法'),
        (CONNECT, 'CONNECT方法'),
        (TRACE, 'TRACE方法'),
    )


class STATUS(object):
    '''接口状态'''
    NEW = 0
    WAIT = 1
    RUNNING = 2
    RAN = 3

    CHOICES = (
        (NEW, u'等待'),
        (WAIT, u'等待'),
        (RUNNING, u'执行中'),
        (RAN, u'已执行'),
    )


class TEST_RESULT(object):
    PASS = 0
    FAIL = 1

    CHOICES = (
        (PASS, u'成功'),
        (FAIL, u'失败'),
    )