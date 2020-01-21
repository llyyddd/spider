import requests
from bs4 import BeautifulSoup
import pymysql
import exDate
from Pic import *
import urllib
from django.contrib import messages
from django.shortcuts import render
from dataApp import models
from catchdata import *
import datetime
# Create your views here.

def aa(req):
    return render(req,"tables.html")
def show(req):
    if req.session.get("user"):
        s_job=req.GET["showjob"]
        if s_job=="人工智能":
            jobs = models.Rjob.objects.all()
        elif s_job=="大数据":
            jobs = models.Djob.objects.all()
        elif s_job=="嵌入式":
            jobs = models.Jjob.objects.all()
        elif s_job=="Python":
            jobs = models.Pjob.objects.all()
        return render(req,"tables.html",locals())
    else:
        return render(req,"login.html")
def refresh(req):
    if req.session.get("user"):
        temp_job = req.GET["j"]
        job=urllib.parse.unquote(temp_job)
        c_job=urllib.parse.unquote(job)
        catch_D(c_job)
        if c_job == "人工智能":
            jobs = models.Rjob.objects.all()
        elif c_job == "大数据":
            jobs = models.Djob.objects.all()
        elif c_job == "嵌入式":
            jobs = models.Jjob.objects.all()
        elif c_job == "Python":
            jobs = models.Pjob.objects.all()
        cur = datetime.datetime.now()
        d = str(cur.ctime())
        messages.success(req, "刷新成功！ 最近刷新时间为："+d)
        return render(req,"tables.html",locals(),)
    else:
        return render(req,"login.html")

def show_p(req):
    if req.session.get("user"):
        jj = req.GET["job"]
        # 将matplotlib图片转换为HTML
        plot_data = make(jj)

        imb = base64.b64encode(plot_data[0])  # 对plot_data进行编码
        ims = imb.decode()
        imd = "data:image/png;base64," + ims

        imb1 = base64.b64encode(plot_data[1])  # 对plot_data进行编码
        ims1 = imb1.decode()
        imd1 = "data:image/png;base64," + ims1

        imb2 = base64.b64encode(plot_data[2])  # 对plot_data进行编码
        ims2 = imb2.decode()
        imd2 = "data:image/png;base64," + ims2

        imb3 = base64.b64encode(plot_data[3])  # 对plot_data进行编码
        ims3 = imb3.decode()
        imd3 = "data:image/png;base64," + ims3

        imb4 = base64.b64encode(plot_data[4])  # 对plot_data进行编码
        ims4 = imb4.decode()
        imd4 = "data:image/png;base64," + ims4
        # iris_im = """<img src="%s">""" % imd
        return render(req, "p.html",locals())
    else:
        return render(req,"login.html")

def index(req):
    return render(req,"index.html")


