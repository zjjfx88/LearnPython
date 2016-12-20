#!/usr/bin/env python
#coding=utf-8

import os
import sys
import time
import json
import httplib
import urllib2
import requests

url = 'http://10.134.100.143:8880/rewrite?last_query=%s&query=%s'

def query_rewrite(last_query, query):
	rewrite = ''
	try:
		h_url = url%(last_query, query)
		response = requests.get(h_url, timeout=2)
		if response:
			obj = json.loads(response.text)
			if obj['rewrite']:
				rewrite = obj['rewrite_query'].encode('utf8')
				print 'last_query:' + last_query + '\tquery:' + query + '\trewrite:' + rewrite
			else:
				file = open('noResult','a+')
				file.write(last_query+'\t'+query+'\n')
				#print 'last_query:' + last_query + '\tquery:' + query + '\trewrite:' + rewrite
	except:
		pass
	return rewrite


def format_query(last_query,query):
	newurl = url%(last_query, query)
	file = open('cibiao1','a+')
	file.write(newurl+'\n')


if __name__ == "__main__":
	inputs = open('qqq', 'r')
	for line in inputs:
		line = line.strip()
		items = line.split('\t')
		if len(items) != 2:
			continue
		last_query = items[0]
		query = items[1]
		format_query(last_query,query)
		#rewrite = query_rewrite(last_query, query)
		#print 'last_query:' + last_query + '\tquery:' + query + '\trewrite:' + rewrite
	inputs.close()
