# -*- coding:utf-8 -*-


class METHOD(object):
    '''requests 请求方法'''
    GET = 1
    POST = 2
    PUT = 3
    DELETE = 4
    HEAD = 5
    CONNECT = 6
    OPTIONS = 7
    TRACE = 8

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
    WAIT = 0
    RUNNING = 1
    RAN = 2

    CHOICES = (
        (WAIT, u'等待'),
        (RUNNING, u'执行中'),
        (RAN, u'已执行'),
    )
