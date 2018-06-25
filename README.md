# DataCheck

### 目录结构
```angular2html
.
├── bin  #执行目录
│   ├── Check.py
│   └── __init__.py
├── conf  #配置目录
│   ├── Config.py
│   ├── Config.pyc
│   ├── __init__.py
│   └── __init__.pyc
├── log   # 日志目录
│   ├── __init__.py
│   └── paramiko.log
├── README.md
└── src   # 源码模块目录
    ├── Color.py
    ├── Color.pyc
    ├── Common.py
    ├── Common.pyc
    ├── Connect.py
    ├── Connect.pyc
    ├── __init__.py
    ├── __init__.pyc
    ├── Kafka.py
    ├── Kafka.pyc
    ├── Online.py
    ├── Online.pyc
    ├── VdsApi.py
    └── VdsApi.pyc

```

### 颜色输出定义

蓝色：标题

绿色：主机名称

紫色：文件名、表名

没有颜色：数据输出

红色：主机之间分隔符


### 变量名字的定义

1、config 配置文件使用'_'连接

2、函数、类都使用大小写驼峰式

3、函数内的变量使用无需使用'_' 连接符


### 配置

修改conf 目录下的Config即可



### 使用
```
cd bin ; python Check.py
````



