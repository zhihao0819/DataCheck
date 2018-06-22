#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/6/22 下午4:24
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : Kafka.py


# from .Common import ShowOutPut
from .Connect import RemoteOper

class KafkaServer(object):
    def __init__(self, host, port, user, passwd, logfile):
        self.remote = RemoteOper(host=host, port=port, username=user,
                            passwd=passwd, logfile=logfile)
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd

















