#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
from urllib import quote

for line in open("ysquery"):
	line=line.strip()
	last_query=quote(line.split('\t')[0])
	query=quote(line.split('\t')[1])
	url="http://10.134.100.143:8880/rewrite?last_query="+last_query+"&query="+query
	with open("newquert","a+") as f:
		f.write(url+"\n")
	

