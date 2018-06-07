#!/usr/bin/python
#-*- conding: utf-8 -*-


import platform
import multiprocessing

print "OS : ", platform.system()
print "Platform : ", platform.platform()
print "OS_Ver :", platform.version()
print "process# :" , platform.processor()
print "CPU# :", multiprocessing.cpu_count()
