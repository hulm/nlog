
# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render_to_response,render,get_object_or_404

from login.models import UserInfo,Assert
from django.db import models
import DB_import
import json
#from django.utils import simplejson
def login(request):
    #username = UserInfo.objects.get(username=admin).username
    #password = UserInfo.objects.get(username=admin).password
    reqMeta = request.META
    #print reqMeta
    if request.method == "POST":
        uname = request.POST.get('username',None)
        pwd = request.POST.get('password',None)
        if UserInfo.objects.filter(username=uname,password=pwd):
            request.session['login_user'] = uname
            return render_to_response('index.html',{'username':uname,'reqMeta':reqMeta})
        else:
            return render_to_response('login.html',{'msg':"用户名或密码错误"})
    return render(request,'login.html')
def logout(request):
    if request.session.get('login_user'):
        del request.session['login_user']
        return render_to_response('login.html')
    else:
        return render_to_response('login.html')
    
    
def user_profile(request):
    username = request.session.get('login_user')
    if username:
        data=UserInfo.objects.all()
        user_list=[]
        for item in data:
            user_list.append(item.username)
        return render_to_response('user_profile.html',{'user_list':data,'username':username})
    else:
        return render_to_response('login.html')
    
def delete(request):
    if request.method == "POST":
        postdata = request.POST
        print postdata['dat'].split(',')[0]
        print postdata['dat'].split(',')[1]
    #print request.POST.get(dat)
        return render_to_response('delete.html',{'postdata':postdata})



def index(request):
    username = request.session.get('login_user',None)
    if username:
        return render_to_response('index.html',{'username':username})
    else:
        return render_to_response('login.html')
        
def register(request):
    return render_to_response('register.html')

def importFile(request):
    f = request.FILES.get('file')
    data = f.readlines()
    return render_to_response('importData.html',{'data':data})


def assert_inside(request,page):
    username = request.session.get('login_user',None)
    if username:
        page=int(page)
        count=Assert.objects.all().count()
        pageCount = count/15
        result=Assert.objects.all()[page*15:(page+1)*15]
        ret = {'data':result,'count':count,'username':username,'pageCount':pageCount,'page':page}
        return render_to_response('assert_inside.html',ret)
    else:
        return  render_to_response('login.html')


def searchDBCheck(request):
    #hosts = ['172.16.8.22','172.16.8.26']
    #dbs = ['ask','news','company','service','showb','solution','vip','quotation','allsite','snippets']
    #ports = ['23022','23004','23038','23025','23001','23044','23029','23008','23000','23046']
    #check_list=[]
    #for host in hosts:
    #    for dbitem in dbs:
    #        port = int(ports[dbs.index(dbitem)])
    #        dbconfig={'host':host,'user':'root','passwd':'','db':'','port':port}
    #        db = DB_import.MySQLHelper(dbconfig)
    #        sql1="select * from "+dbitem
    #        resault = db.NoneExcuteQuerySQL(sql1)
    #        #checkres = ("host %s,,ports%s,db:%s,num:%s") % (host,port,dbitem,resault)
    #        checkres = {'host':host,'port':port,'dbname':dbitem,'num':resault}
    #        check_list.append(checkres)
    return render_to_response("searchCheck.html")
    #ret = json.dumps(check_list)
    #print ret
    #return ret


def searchDBCheck1(request):
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
    #return render_to_response("searchCheck.html",{'data':json.dumps(check_list)})
    print check_list
    return HttpResponse(json.dumps(check_list), content_type="application/json")