# -*- coding:utf-8 -*-

from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    print 'name',name,'addr',addr
    return formataddr((\
        Header(name,'utf-8').encode(),\
        addr.encode('utf-8') if isinstance(addr,unicode) else addr))

# 通过SMTP发出去
# 输入email地址和口令
from_addr = raw_input('From:')
password = raw_input('Password:')
# 输入smtp服务器
smtp_server = raw_input('SMTP server:')
# 输入收件人地址
to_addr = raw_input('To:')

# 构造邮件内容，注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'，
# 最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
msg = MIMEText('hello,send by Python...','plain','utf-8')

# 发送html，在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')

msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……','utf-8').encode()

# SMTP协议默认端口是25
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()