#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/6/22 下午6:17
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : color.py

class ShowOutPut(object):

    def Normal(self, message):
        '''display normal data'''
        return message

    def Blue(self, message):
        '''display task title'''
        return "\033[1;34m %s \033[0m" % message

    def Green(self, message):
        '''display host title'''
        return "\033[1;32m %s \033[0m" % message

    def Purple(self, message):
        '''display filename or table'''
        return "\033[1;35m %s \033[0m" % message

    def Red(self, message):
        '''hosts split character'''
        return "\033[1;31m %s \033[0m" % message
