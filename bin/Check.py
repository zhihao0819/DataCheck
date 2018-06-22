#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/6/21 下午5:13
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : Check.py

import sys
sys.path.append('../')
from conf import Config
from src.Common import ManyHandle



def CheckApi():
    api = ManyHandle(user=Config.user, port=Config.port, passwd=Config.passwd, logfile=Config.log_file)
    api.ApiHandle(hosts=Config.api_servers, datadir=Config.data_dir)

def main():
    CheckApi()


if __name__ == '__main__':
    main()




