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

def CheckKafka():
    kafka = ManyHandle(user=Config.user, port=Config.port, passwd=Config.passwd, logfile=Config.log_file)
    # just only one zookeeper host, because config file zk is tuple.
    kafka.KafkaHandle(hosts=Config.kafka_servers, zkhost=Config.zk_servers[0], zkport=Config.zk_port, topic=Config.kafka_topic,
                      kabin=Config.kafka_bin, kaconsumer=Config.kafka_cmd)

def CheckOnline():
    online = ManyHandle(user=Config.user, port=Config.port, passwd=Config.passwd, logfile=Config.log_file)
    online.OnlineHandle(hosts=Config.online_servers, sparkbin=Config.spark_bin, sparkcmd=Config.spark_cmd,
                        tables=Config.tables, tempsql=Config.temp_sql)


def main():
    CheckApi()
    CheckKafka()
    CheckOnline()

if __name__ == '__main__':
    main()




