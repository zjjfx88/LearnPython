# -*- coding:utf-8 -*-
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from email.utils import parseaddr,formataddr
from email.header import Header
from email.mime.text import MIMEText
from email import encoders
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    print 'name',name,'addr',addr
    return formataddr((\
        Header(name,'utf-8').encode(),\
        addr.encode('utf-8') if isinstance(addr,unicode) else addr))

# 输入email地址和口令
from_addr = raw_input('From:')
password = raw_input('Password:')
# 输入smtp服务器
smtp_server = raw_input('SMTP server:')
# 输入收件人地址
to_addr = raw_input('To:')

# 邮件对象
msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……','utf-8').encode()
# 邮件正文
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('D:\\python\\PyProject\\LearnPython\\blur.jpg','rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image','jpg',filename='blur.jpg')
    # 加上必要的头信息
    mime.add_header('Content-Disposition','attachment',filename='blur.jpg')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来
    mime.set_payload(f.read())
    # 用base64编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

# SMTP协议默认端口是25
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()