# -*- coding: utf-8 -*-
#文件读取
file = open('text.txt','r')
#read(),一次性把所有数据读入内存中
read_content = file.read()
print 'read_content',read_content
print '#'*80
file.close()


file2 = open('text.txt','r')
#readline(),一次读取一行
read_lineContent = file2.readline()
print 'read_lineContent',read_lineContent
print '#'*80
file2.close()


file3 = open('text.txt','r')
#readlines(),一次读取所有行
read_lines_content = file3.readlines()
print 'read_lines_content',read_lines_content
print '#'*80
file3.close()