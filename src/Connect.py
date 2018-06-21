#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/6/21 上午10:56
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : check.py

import sys, paramiko
sys.path.append('../')
from conf import Config

def RemoteCommand(host,
                  port,
                  username,
                  passwd,
                  command,
                  logfile=Config.log_file):

    paramiko.util.log_to_file(logfile)
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    conn.connect(hostname=host, port=port, username=username, password=passwd)
    stdin, stdout, stderr = conn.exec_command(command)
    stdin.write('Y')
    response = stdout.read()
    conn.close()
    return response


































