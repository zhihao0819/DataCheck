#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/6/22 下午2:52
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : Common.py

from .VdsApi import ApiServer

class ShowOutPut(object):

    def Normal(self, message):
        return message

    def Blue(self, message):
        return "\033[1;34m %s \033[0m" % message

    def Green(self, message):
        return "\033[1;32m %s \033[0m" % message

    def Purple(self, message):
        return "\033[1;35m %s \033[0m" % message

    def Red(self, message):
        return "\033[1;31m %s \033[0m" % message


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































