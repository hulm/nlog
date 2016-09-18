#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
class MySQLHelper:
    def __init__(self,host,user,password,db,port):
        try:
            self.conn=MySQLdb.connect(host=host,user=user,passwd=password,db=db,port=port)
        except MySQLdb.Error as e:
            print ("Mysql Error %d: %s" % (e.args[0],e.args[1]))

    def excuteSQL(self,sql):
        self.cur = self.conn.cursor()
        resault=self.cur.execute(sql)
        return resault
    def fetchAllRows(self):
        return self.cur.fetchall()
if __name__ == '__main__':
    db = MySQLHelper('192.168.0.235','root','','nlog',3306)
    sql="select * from login_userinfo"
    db.excuteSQL(sql)
    result = db.fetchAllRows();
    print result