#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/6/21 下午5:13
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : Check.py

import sys
sys.path.append('../')
from src.VdsApi import ApiServer

def CheckApi():
    api = ApiServer()
    api.Show()

def main():
    CheckApi()


if __name__ == '__main__':
    main()




