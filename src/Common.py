#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/6/22 下午2:52
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : Common.py

from .VdsApi import ApiServer
from .Color import ShowOutPut

class ManyHandle(object):

    def __init__(self, user, port, passwd, logfile):
        self.user = user
        self.port = port
        self.passwd = passwd
        self.logfile = logfile

    def ApiHandle(self, hosts, datadir):
        mess = ShowOutPut()
        mess.Blue('################ Check vds-api Servers Data  #######################')
        for host in hosts:
            api = ApiServer(host=host, port=self.port, user=self.user, passwd=self.passwd, logfile=self.logfile)
            api.Show(datadir)































