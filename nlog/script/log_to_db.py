#!/usr/bin/env python
# -*- coding:utf-8 —*-
import sys
import os

class LogToMysql:
    def __init__(self,log_path):
	self.log_path = log_path
    
    def getFilelist(self):
	filelist=[]
	for file in os.listdir(self.log_path):
	    filelist.append(self.log_path+'/'+file)
	return filelist



    def Log_Analysis(self):
	count_404 = 0
	count_500 = 0
	ip = 0
	pv = 0
	filelist = self.getFilelist()
	print filelist

log = LogToMysql("/data/woyaoce/201605")

log.Log_Analysis()
