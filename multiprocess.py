# -*- coding:utf-8 -*-

from multiprocessing import Process
import os

def rum_proc(name):
    print 'Run child process %s (%s)……' % (name, os.getpid())

if __name__ == '__main__':
    print 'Parent process %s .' % os.getpid()
    p = Process(target=rum_proc, args=('test',))
    print 'Process will start'
    p.start()
    p.join()
    print 'Process end.'