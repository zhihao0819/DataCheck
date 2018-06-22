#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/6/22 下午2:52
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : Common.py


class ShowOutPut(object):

    def Normal(self, message):
        return message

    def Green(self, message):
        return "\033[1;32m %s \033[0m" % message

    def Purple(self, message):
        return "\033[1;35m %s \033[0m" % message

    def Red(self, message):
        return "\033[1;31m %s \033[0m" % message























