#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/6/21 下午5:30
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : VdsApi.py

import sys
from .Connect import RemoteCommand
from .Common import ShowOutPut
sys.path.append('../')
from conf import Config

def GetApiHosts():
    apihosts = Config.api_servers
    return apihosts

def GetApiLogsPath():
    apihosts = GetApiHosts()
    command = 'ls %s/*.log' % Config.data_dir
    logspath = RemoteCommand(host=apihosts[0], port=Config.api_port, username=Config.api_user,
                             passwd=Config.api_passwd, command=command)
    return logspath.strip('\n').split('\n')

def GetApiLogsData():
    apihosts = GetApiHosts()
    logspath = GetApiLogsPath()
    datas, h, l = [], {} , {}
    for host in apihosts:
        for log in logspath:
            command = 'tail -2 %s' % log
            logsdata = RemoteCommand(host=host, port=Config.api_port, username=Config.api_user,
                                     passwd=Config.api_passwd, command=command)
            l[log] = logsdata
        h[host] = l
    datas.append(h)
    return datas

def Show():
    resdatas = GetApiLogsData()
    mess = ShowOutPut()
    for datas in resdatas:
        for host in datas.keys():
            print mess.Green('## %s ##' % host)
            for f in datas[host].keys():
                print mess.Purple('# %s' % f)
                print mess.Normal(datas[host][f])
            print mess.Red("################################\n")









