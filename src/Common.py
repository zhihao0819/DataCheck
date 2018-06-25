#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/6/22 下午2:52
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : Common.py

from .VdsApi import ApiServer
from .Kafka import KafkaServer
from .Online import OnlineServer
from .Color import ShowOutPut

class ManyHandle(object):

    def __init__(self, user, port, passwd, logfile):
        self.user = user
        self.port = port
        self.passwd = passwd
        self.logfile = logfile

    def ApiHandle(self, hosts, datadir):
        mess = ShowOutPut()
        print mess.Blue('################ Check vds-api Servers Data  #######################')
        for host in hosts:
            api = ApiServer(host=host, port=self.port, user=self.user, passwd=self.passwd, logfile=self.logfile)
            api.Show(datadir)


    def KafkaHandle(self, hosts, zkhost, zkport, topic, kabin, kaconsumer):
        mess = ShowOutPut()
        print mess.Blue('################ Check Kakfa-services Servers Data  #######################')
        for host in hosts:
            kafka = KafkaServer(host=host, port=self.port, user=self.user, passwd=self.passwd, logfile=self.logfile)
            kafka.Show(zkhost=zkhost, zkport=zkport, topic=topic, kabin=kabin, kaconsumer=kaconsumer)


    def OnlineHandle(self, hosts, sparkbin, sparkcmd, tables, tempsql):
        mess = ShowOutPut()
        print mess.Blue('################ Check Online-Hive Tables Data  #######################')
        for host in hosts:
            online = OnlineServer(host=host, port=self.port, user=self.user, passwd=self.passwd, logfile=self.logfile)
            online.Show(sparkbin=sparkbin, sparkcmd=sparkcmd, tables=tables, tempsql=tempsql)





























