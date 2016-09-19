"""nlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from nlog.views import current_time,log
from login.views import login,index,register,delete,user_profile,logout,importFile,assert_inside,searchDBCheck
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^time/', current_time),
    url(r'^log/', log),
    url(r'^login/$', login),
    url(r'^index/', index),
    url(r'^register/',register),
	url(r'^delete/',delete),
    url(r'^user_profile/',user_profile),
    url(r'^logout/',logout),
    url(r'^importFile/',importFile),
    url(r'^assert_inside/(?P<page>\d+)',assert_inside),
    url(r'^searchDBCheck/',searchDBCheck),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': 'E:\\bootstraptest\\nlog\\templates'}),
]
