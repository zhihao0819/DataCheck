#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/6/25 上午10:49
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : Online.py

import time
from .Color import ShowOutPut
from .Connect import RemoteOper


class OnlineServer(object):
    def __init__(self, host, port, user, passwd, logfile):
        self.remote = RemoteOper(host=host, port=port, username=user,
                                 passwd=passwd, logfile=logfile)
        self.host = host

    def CreateSqlFile(self, tempsql, table):
        querytm = time.strftime('%Y%m%d%H%')
        self.remote.Command('''
            echo "select * from gio.%s WHERE time like %s order by stm desc limit 10;" > %s''' % (table, querytm, tempsql))

    def GetDHiveData(self, sparkbin, sparkcmd, table, tempsql):
        self.CreateSqlFile(tempsql, table)
        command = 'cd %s && ./%s --master local[4] -f %s' % (sparkbin, sparkcmd, tempsql)
        print command
        datas = self.remote.Command(command)
        return datas

    def Show(self, sparkbin, sparkcmd, tables, tempsql):
        mess = ShowOutPut()
        print mess.Green('## %s ##' % self.host)
        for table in tables:
            datas = self.GetDHiveData(sparkbin, sparkcmd, table, tempsql)
            print mess.Purple('# %s' % table)
            print mess.Normal(datas)
        print mess.Red('========================================\n')

