# -*- coding:utf-8 -*-

# 创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，
# 就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket对象就创建成功，但是还没有建立连接。
import socket

#创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
s.connect(('www.sina.com.cn', 80))

# 发送数据
s.send('GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')

# 接收数据
buffer = []
while True:
    #每次最多接受1k字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = ''.join(buffer)

# 关闭连接
s.close()

# 接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件：
header, html = data.split('\r\n\r\n', 1)
print header
# 把接受的数据存入文件
with open('sina.html','wb') as f:
    f.write(html)