#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/6/21 上午10:56
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : check.py

import paramiko

class RemoteOper(object):
    def __init__(self, host, port, username, passwd, logfile):
        self.host = host
        self.port = port
        self.username = username
        self.passwd = passwd
        self.logfile = logfile


    def Command(self, command):
        paramiko.util.log_to_file(self.logfile)
        conn = paramiko.SSHClient()
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        conn.connect(hostname=self.host, port=self.port,
                     username=self.username, password=self.passwd)
        stdin, stdout, stderr = conn.exec_command(command)
        stdin.write('Y')
        response = stdout.read()
        conn.close()
        return response


































