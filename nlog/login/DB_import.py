#!/usr/bin/env python
#-*- coding:utf-8 -*
import MySQLdb
class MySQLHelper():
    def __init__(self,dbconfig):
        self.host=dbconfig['host']
        self.user=dbconfig['user']
        self.passwd=dbconfig['passwd']
        self.db=dbconfig['db']
        self.port=dbconfig['port']
    def MySQLConn(self):
        try:
            self.conn = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,port=self.port)
            #self.cur = self.conn.cursor()
            return self.conn
        except Exception as e:
            print("host:%s,port:%d connect timeout") %(self.host,self.port)
     
    def NoneExcuteQuerySQL(self,sql):
        conn = self.MySQLConn()
        if conn:
            cur = conn.cursor()
        #cur = conn.cursor()
        try:
            return cur.execute(sql)
        except Exception as e:
            print("host:%s,port:%d connect timeout") %(self.host,self.port)
        # finally:
            # cur.close()
            # self.conn.commit()
            # self.conn.close()
    def ExcuteQuerySQL(self,sql):
        conn = self.MySQLConn()
        cur = conn.cursor()
        #cur = conn.cursor()
        try:
            cur.execute(sql)
            return cur.fetchall()
            #return resault
        except Exception as e:
            print ("行Mysql: %s 时出错：%s" % (sql,e))
        # finally:
            # cur.close()
            # self.conn.commit()
            # self.conn.close()
        
    def NoneExcuteManyQuerySQL(self,sql,values):
        conn = self.MySQLConn()
        cur = conn.cursor()
        #cur = conn.cursor()
        try:
            cur.executemany(sql,values)
        except Exception as e:
            print ("行Mysql: %s 时出错：%s" % (sql,e))
        # finally:
            # cur.close()
            # self.conn.commit()
            # self.conn.close()

if __name__ == '__main__':
    dbconfig={'host':'192.168.0.235','user':'root','passwd':'','db':'nlog','port':3306}
    print dbconfig['passwd']
    db = MySQLHelper(dbconfig)
    sql = "insert into login_assert(department,number,type,model,brand,user,position) values('','10-01','显示器','E1920','三星','备用','库房')"
    db.NoneExcuteQuerySQL(sql)
