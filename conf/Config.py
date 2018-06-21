#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/6/21 上午10:46
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : config.py

#common config
ansible_dir = '/opt/growing-ansible/inventories/01-690cfg'
log_file = '../log/paramiko.log'
jump_server = 'front0'


#vds-api config
api_servers = ('api0', 'api1')
# api_servers = 'front0'
api_user = 'apps'
api_port = 22
api_passwd = None
data_dir = '/data/vds-api/event-logs'











