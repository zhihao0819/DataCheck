#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/6/21 上午10:46
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : config.py

# common config
log_file = '../log/paramiko.log'
user = 'apps'
port = 22
passwd = None
zk_servers = ('kafka0', 'kafka1', 'kafka2')
zk_port = 2181

# vds-api config
api_servers = ('api0', 'api1')
data_dir = '/data/vds-api/event-logs'

# kafka config
kafka_servers = ('kafka0', 'kafka1', 'kafka2')
kafka_bin = '/apps/svr/kafka/bin'
kafka_topic = 'vds-api-web-pv'
kafka_cmd = 'kafka-console-consumer.sh'

# online config
online_servers = ('online0', 'online1')
tables = ('visit', 'action', 'page')
spark_bin = '/apps/svr/spark/bin'
spark_cmd = './spark-sql'
temp_sql = '/tmp/.sql'

















