#!/usr/bin/python
#-*- coding: utf-8 -*-



import socket
host= socket.gethostbyname_ex("www.google.com")

print "\n ------------------ Host info --------"
print host

print "\n ----------------- Host one line-====="
for i in host :
	print i

(hostname, aliaslist, ipaddrlist) = host
print "\n ------------------ IP  addr -------"
print "ip :", ipaddrlist[0]
