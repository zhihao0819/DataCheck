#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/6/21 下午5:30
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : VdsApi.py

import sys
from .Connect import RemoteCommand
sys.path.append('../')
from conf import Config

def GetApiHosts():
    apihosts = Config.api_servers
    return apihosts

def GetApiLogsPath():
    apihosts = GetApiHosts()
    command = 'ls %s/*.log' % Config.data_dir
    logspath = RemoteCommand(host=apihosts[0], port=Config.api_port, username=Config.api_user, passwd=Config.api_passwd, command=command)
    return logspath.strip('\n').split('\n')

def GetApiLogsData():
    logspath = GetApiLogsPath()
    # print logspath
    for log in logspath:
        command = 'tail -2 %s' % log
        print command














