# -*- coding:utf-8 -*-
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server

# 导入编写的WSGI_Hello.py函数
from WSGI_Hello import application

# 创建一个服务器，ip地址为空，端口是8000，处理函数是application
httpd = make_server('',8000,application)
print "Serving Http on port 8000"
# 开始监听HTTP请求
httpd.serve_forever()