# -*- coding:utf-8 -*-

import hashlib
md5 = hashlib.md5()
password = 'zjjfx88'
hs1 = md5.update(password)
print md5.hexdigest()
pwd_input = raw_input('请输入密码：')

if md5.update(pwd_input) == md5.update(password):
    print 'Yes'
else:
    print 'No'