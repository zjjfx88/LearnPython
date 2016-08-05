# -*- coding:utf-8 -*-

import os

print 'Process (%s) start……' % os.getpid()

pid = os.fork()
# 尽在linux下可以运行，返回两个进程，一个父进程，一个子进程，子进程pid=0，父进程就是当前运行程序的进程号
if pid == 0 :
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(),pid)