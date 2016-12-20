#/bin/bash


time=`date +%Y_%m_%d`
grep "GET /rewrite?" data/qrw.err.log* | awk -F 'GET ' '{print $2}' |awk -F " HTTP" '{print $1}' >> query_$time
