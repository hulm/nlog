#!/usr/bin/env python
# -*- coding: utf-8 -*-
import DB_import
hosts = ['172.16.8.22','172.16.8.26']
dbs = ['ask','news','company','service','showb','solution','vip','quotation','allsite','snippets']
ports = ['23022','23004','23038','23025','23001','23044','23029','23008','23000','23046']
check_list=[]
for host in hosts:
    for dbitem in dbs:
        port = int(ports[dbs.index(dbitem)])
        dbconfig={'host':host,'user':'root','passwd':'','db':'','port':port}
        db = DB_import.MySQLHelper(dbconfig)
        sql1="select * from "+dbitem
        resault = db.NoneExcuteQuerySQL(sql1)
        #checkres = ("host %s,,ports%s,db:%s,num:%s") % (host,port,dbitem,resault)
        checkres = {'host':host,'port':port,'dbname':dbitem,'num':resault}
        check_list.append(checkres)
        print checkres
print check_list