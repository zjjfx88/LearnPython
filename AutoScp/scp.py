#!/usr/bin/python
import os,re

class RemoteShell:
	def __init__(self,host,user,pwd):
		self.host=host
		self.user=user
		self.pwd=pwd


	def put(self,local_path,remote_path):
		scp_put='''
			spawn scp %s@%s:%s %s
			expect "(yes/no)?" {
			send "yes\r"
			expect "password:"
			send "%s\r"
			} "password:" {send "%s\r"}
			expect eof
			exit'''
		os.system("echo '%s'>scp_put.cmd" % (scp_put % (self.user,self.host,remote_path,os.path.expanduser(local_path),self.pwd,self.pwd)))
		
		os.system('expect scp_put.cmd')
	
		os.system('rm scp_put.cmd')


def main():
	host_list=['qrw01.wap.djt.ted','qrw01.wap.gd.ted','qrw01.wap.tc.ted','qrw02.wap.djt.ted','qrw02.wap.gd.ted','qrw02.wap.tc.ted']
	for host in host_list:
		scp_init = RemoteShell(host,'guest','Sogou@)!$')
		scp_init.put('./data','/search/odin/daemon/qrw/log/history/*')
		os.system('sh awk_cmd.sh')
		os.system('rm -rf data/*')


if __name__ == '__main__':
	main()
	
