from django.shortcuts import render_to_response
import os
import datetime
import json

def current_time(request):
    time = datetime.datetime.now()
    return render_to_response('current_time.html',{'current_time':time})


def log(request):
	filelist=[]
	filenames  = os.listdir(r'/data/woyaoce/201606/')
	dic_404 = {}
	dic_500 = {}
	count_404 = 0
	count_500 = 0
	day_list=[]
	for filename in filenames:
	    filedate = filename.split('-')[0]+filename.split('-')[1]+filename.split('-')[2]
	    for line in open('/data/woyaoce/201606/'+filename).readlines():
	        if " 404 " in line:
       	              count_404 = count_404 + 1
	        if " 500 " in line:
       		      count_500 = count_500 + 1
        	dic_404[filedate] = count_404
       	        dic_500[filedate] = count_500
	    day_list.append(filename.split('-')[2])	
	#day_list.append('12')
	sort_day_list = sorted(day_list)
	data = str(sorted(day_list)).decode("unicode-escape")
	sort_dic_404 = dict(sorted(dic_404.items()))
	sort_dic_500 = dict(sorted(dic_500.items()))
	list_404=[]
	list_500=[]
	for key,value in sort_dic_404.items():
		list_404.append(value)
	for key,value in sort_dic_500.items():
		list_500.append(value)
	#return render_to_response('log.html',{'log404':json.dumps(list_404),'log500':json.dumps(list_500)})
	return render_to_response('log.html',{'data':data,'log404':list_404,'log500':list_500})
