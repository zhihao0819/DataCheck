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


class ApiServer(object):
    def __init__(self):
        self.apihosts = Config.api_servers

    def GetApiLogsPath(self):
        command = 'ls %s/*.log' % Config.data_dir
        logspath = RemoteCommand(host=self.apihosts[0], port=Config.port, username=Config.user,
                                 passwd=Config.passwd, command=command)
        return logspath.strip('\n').split('\n')

    def GetApiLogsData(self):
        logspath = self.GetApiLogsPath()
        datas, h, l = [], {} , {}
        for host in self.apihosts:
            for log in logspath:
                command = 'tail -2 %s' % log
                logsdata = RemoteCommand(host=host, port=Config.port, username=Config.user,
                                         passwd=Config.passwd, command=command)
                l[log] = logsdata
            h[host] = l
        datas.append(h)
        return datas

    def Show(self):
        resdatas = self.GetApiLogsData()
        mess = ShowOutPut()
        print mess.Blue('################ Check vds-api Servers Data  #######################')
        for datas in resdatas:
            for host in datas.keys():
                print mess.Green('## %s ##' % host)
                for f in datas[host].keys():
                    print mess.Purple('# %s' % f)
                    print mess.Normal(datas[host][f])
                print mess.Red("========================================\n")









