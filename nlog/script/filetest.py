#!/usr/bin/env python
#coding:utf-8
import sys,os
from DB_import import *
dbconfig={'host':'192.168.0.235','user':'root','passwd':'','db':'nlog','port':3306}
db = MySQLHelper(dbconfig)
#sql = "insert into login_assert(department,number,type,model,brand,user,position) values(%s,%s,%s,%s,%s,%s,%s)"
#sql = "insert into login_assert values(%s,%s,%s,%s,%s,%s,%s,%s)"
#db.NoneExcuteManyQuerySQL(sql,rowlist)

f = open(r'C:\Users\hulm\Desktop\2016.txt')
rowlist=[]
tmplist = []
for line in f.readlines():
    #for i in range(7):
     #   tmplist.append(str(line.split()[i]))
     #   print str(line.split()[i])
    sql = "insert into login_assert(department,number,type,model,brand,user,position) values(%s,%s,%s,%s,%s,%s,%s)" %("'"+str(line.split()[0])+"'","'"+str(line.split()[1])+"'","'"+str(line.split()[2])+"'","'"+str(line.split()[3])+"'","'"+str(line.split()[4])+"'","'"+str(line.split()[5])+"'","'"+str(line.split()[6])+"'")
    db.NoneExcuteQuerySQL(sql)
    #print tuple(tmplist)
   # print tmplist
    #rowlist.append(tuple(tmplist))
    #tmplist = []
#print rowlist
f.close()
#print rowlist
#dbconfig={'host':'192.168.0.235','user':'root','passwd':'','db':'nlog','port':3306}
#db = MySQLHelper(dbconfig)
#sql = "insert into login_assert(department,number,type,model,brand,user,position) values(%s,%s,%s,%s,%s,%s,%s)"
#sql = "insert into login_assert values(%s,%s,%s,%s,%s,%s,%s,%s)"
#db.NoneExcuteManyQuerySQL(sql,rowlist)
