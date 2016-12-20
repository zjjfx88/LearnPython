#!/usr/bin/python
import re
import sys

if len(sys.argv)!=2:
    print ("input Error!!!\npython logP.py file1")
    exit(1)

log = sys.argv[1]

f = open(log)
for line in f:
    line = line.strip()
    response_type = re.search(r',returntype=(\w+),',line)
    request_type = re.search(r'&class=(\w+)&',line)
    uri = re.search(r'uri=(.+?),',line)
    if not response_type or not request_type:
        print "response_type or request_type is not exsit ! log is :\n" + line
        try:
            if response_type.group(1) != request_type.group(1):
                print ("response_type="+response_type.group(1)+" and request_type="+request_type.group(1))
                print uri.group(1)
        except:
            pass
f.close()



