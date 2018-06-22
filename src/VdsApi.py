#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/6/21 下午5:30
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : VdsApi.py


from .Connect import RemoteOper
from .Color import ShowOutPut

class ApiServer(object):
    def __init__(self, host, port, user, passwd, logfile):
        self.remote = RemoteOper(host=host, port=port, username=user,
                            passwd=passwd, logfile=logfile)
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd

    def GetApiLogsPath(self, datadir):
        command = 'ls %s/*.log' % datadir
        logspath = self.remote.Command(command)
        return logspath.strip('\n').split('\n')

    def GetApiLogsData(self, datadir):
        logspath = self.GetApiLogsPath(datadir)
        logs = {}
        for log in logspath:
            command = 'tail -2 %s' % log
            logsdata = self.remote.Command(command)
            logs[log] = logsdata
        return {self.host: logs}


    def Show(self, datadir):
        resdatas = self.GetApiLogsData(datadir)
        mess = ShowOutPut()
        # print mess.Blue('################ Check vds-api Servers Data  #######################')

        print mess.Green('## %s ##' % self.host)
        for file in resdatas[self.host].keys():
            print mess.Purple('# %s' % file)
            print mess.Normal(resdatas[self.host][file])

        print mess.Red("========================================\n")









