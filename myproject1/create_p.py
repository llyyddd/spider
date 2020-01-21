import pandas as pd
from sqlalchemy import create_engine
from matplotlib.pyplot import MultipleLocator
import matplotlib.pyplot  as plt
import matplotlib as mp
from nnum import *
import pymysql
import numpy as np


def com(jj):
    if jj == "Rjob":
        j = "人工智能"
    elif jj == "Djob":
        j = "大数据"
    elif jj == "Jjob":
        j = "嵌入式"
    elif jj == "Pjob":
        j = "Python"
    com = create_engine("mysql+pymysql://root:root@localhost:3306/sx")
    s = "select  city,COUNT(DISTINCT company) as sumnumber from {}  group by city"
    sql = s.format(jj)
    df = pd.read_sql_query(sql, com)
    mp.rcParams["font.family"] = "Microsoft YaHei"  # 默认 sans-serif
    mp.rcParams["font.size"] = 15  # 默认10
    clist = df["city"]  # 定义两个列表
    nlist = df["sumnumber"]
    x = []
    y = []
    d = dict(zip(clist, nlist))
    list = sorted(d.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)  # 得到的是一个list,list中的元素是tuple
    for i in list:
        x.append(i[0])  # 把元组中的第一个值添加到x中
        y.append(i[1])  # 把元组中的第二个值添加到y中
    plt.figure(figsize=(20, 12), facecolor="#F1F5FB", dpi=80)
    plt.bar(x, y, color='coral', width=0.5)
    plt.xlabel("城市", fontsize=14)
    plt.ylabel("有招聘职位的公司数", fontsize=14)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    y_major_locator = MultipleLocator(10)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax = plt.gca()
    # ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    # 把x轴的主刻度设置为1的倍数
    ax.yaxis.set_major_locator(y_major_locator)
    # 把y轴的主刻度设置为10的倍数
    plt.xlim(-0.5, len(x))
    # 把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
    plt.ylim(0, max(y) + 5)
    # 把y轴的刻度范围设置为0到70，同理，-5不会标出来，但是能看到一点空白
    plt.xticks(rotation=90)

    temp = zip(x, y)
    for x, y in temp:
        plt.text(x, y + 2, y, ha="center", va="top")

    plt.title("{}各个城市需要招聘的公司数".format(j), fontsize=14)
    plt.savefig("city_com.png")
    return plt



def jt(jj):
    com = create_engine("mysql+pymysql://root:root@localhost:3306/sx")
    s = "select  city,COUNT(DISTINCT jobtype) as sumnumber from {}  group by city"
    sql = s.format(jj)
    df = pd.read_sql_query(sql, com)
    if jj == "Rjob":
        j = "人工智能"
    elif jj == "Djob":
        j = "大数据"
    elif jj == "Jjob":
        j = "嵌入式"
    elif jj == "Pjob":
        j = "Python"
    mp.rcParams["font.family"] = "Microsoft YaHei"  # 默认 sans-serif
    mp.rcParams["font.size"] = 15  # 默认10
    clist = df["city"]  # 定义两个列表
    nlist = df["sumnumber"]
    x = []
    y = []
    d = dict(zip(clist, nlist))
    list = sorted(d.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)  # 得到的是一个list,list中的元素是tuple
    for i in list:
        x.append(i[0])  # 把元组中的第一个值添加到x中
        y.append(i[1])  # 把元组中的第二个值添加到y中
    plt.figure(figsize=(20, 12), facecolor="#F1F5FB", dpi=80)
    plt.bar(x, y, color='lightsteelblue', width=0.5)
    plt.xlabel("城市", fontsize=14)
    plt.ylabel("需求职位数", fontsize=14)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    y_major_locator = MultipleLocator(10)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax = plt.gca()
    # ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    # 把x轴的主刻度设置为1的倍数
    ax.yaxis.set_major_locator(y_major_locator)
    # 把y轴的主刻度设置为10的倍数
    plt.xlim(-0.5, len(x))
    # 把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
    plt.ylim(0, max(y) + 10)
    # 把y轴的刻度范围设置为0到70，同理，-5不会标出来，但是能看到一点空白
    plt.xticks(rotation=90)

    temp = zip(x, y)
    for x, y in temp:
        plt.text(x, y + 1, y, ha="center", va="top")

    plt.title("{}各个城市需求的职位数".format(j), fontsize=14)
    plt.savefig("city_jt.png")
    return plt

def zt(jj):
    com = create_engine("mysql+pymysql://root:root@localhost:3306/sx")
    s = "select  recruittype,COUNT( recruittype) as sumnumber from {}  group by recruittype"
    sql=s.format(jj)
    df = pd.read_sql_query(sql, com)
    if jj == "Rjob":
        j = "人工智能"
    elif jj == "Djob":
        j = "大数据"
    elif jj == "Jjob":
        j = "嵌入式"
    elif jj == "Pjob":
        j = "Python"
    mp.rcParams["font.family"] = "Microsoft YaHei"  # 默认 sans-serif
    mp.rcParams["font.size"] = 18  # 默认10
    lables = df["recruittype"]  # 定义两个列表
    facs = df["sumnumber"]
    colors = ['coral', 'lightskyblue']
    explode = [0, 0.1]
    plt.figure(figsize=(8, 7), facecolor="#F1F5FB", dpi=80)
    plt.pie(x=facs, labels=lables, explode=explode, colors=colors, labeldistance=1.1, pctdistance=0.6, startangle=90,
            autopct='%1.1f%%')
    plt.legend(loc="best", fontsize=10, bbox_to_anchor=(1, 1), borderaxespad=0.5)
    plt.title("{}招聘类型比率".format(j))
    plt.savefig("ztype.png")
    return plt
from wordcloud import  WordCloud
def ct(jj):
    con = pymysql.connect("localhost", "root", "root", "sx", charset='utf8')  # 链接
    db = con.cursor()
    com = create_engine("mysql+pymysql://root:root@localhost:3306/sx")
    s = "select city,neednum from {} "
    sql=s.format(jj)
    df = pd.read_sql_query(sql, com)
    mp.rcParams["font.family"] = "Microsoft YaHei"  # 默认 sans-serif
    mp.rcParams["font.size"] = 15  # 默认10
    tlist = df["city"]  # 定义两个列表
    nlist = df["neednum"]
    sql = "truncate table j"
    db.execute(sql)
    con.commit()
    for i in range(1, len(nlist)):
        number = int(change_to_num(nlist[i]))
        sql1 = "insert into j(neednum,city) values('%d','%s')" % (number, tlist[i])
        db.execute(sql1)
        con.commit()
    db.close()
    con.close()
    sql = "select city,sum(neednum) as sum from j group by city "
    df = pd.read_sql_query(sql, com)
    tlist = df["city"]  # 定义两个列表
    nlist = df["sum"]
    d = dict(zip(tlist, nlist))
    list = sorted(d.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    x = []  # 城市
    y = []  # 需求人数
    for i in list:
        x.append(i[0])
        y.append(int(i[1]))
    plt.figure(figsize=(20, 12), facecolor="#F1F5FB", dpi=80)
    plt.bar(x, y, color='lightpink')
    plt.xlabel("城市", fontsize=14)
    plt.ylabel("需求人数", fontsize=14)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    y_major_locator = MultipleLocator(50)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax = plt.gca()
    # ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    # 把x轴的主刻度设置为1的倍数
    ax.yaxis.set_major_locator(y_major_locator)
    # 把y轴的主刻度设置为10的倍数
    plt.xlim(-0.5, len(x))
    # 把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
    plt.ylim(0, max(y) + 5)
    # 把y轴的刻度范围设置为0到70，同理，-5不会标出来，但是能看到一点空白
    plt.xticks(rotation=90)

    temp = zip(x, y)
    for x, y in temp:
        plt.text(x, y + 10, y, ha="center", va="top")
    if jj == "Rjob":
        j = "人工智能"
    elif jj == "Djob":
        j = "大数据"
    elif jj == "Jjob":
        j = "嵌入式"
    elif jj == "Pjob":
        j = "Python"
    plt.title("{}城市需求人数柱状图".format(j), fontsize=14)
    plt.savefig("p.png")
    return plt

def nn(jj):
    con = pymysql.connect("localhost", "root", "root", "sx", charset='utf8')  # 链接
    db = con.cursor()
    com = create_engine("mysql+pymysql://root:root@localhost:3306/sx")
    s = "select pubtime,neednum from {} "
    sql=s.format(jj)
    df = pd.read_sql_query(sql, com)
    mp.rcParams["font.family"] = "Microsoft YaHei"  # 默认 sans-serif
    mp.rcParams["font.size"] = 15  # 默认10
    tlist = df["pubtime"]  # 定义两个列表
    nlist = df["neednum"]
    sql = "truncate table j"
    db.execute(sql)
    con.commit()
    print(tlist)
    for i in range(0, len(nlist)):
        number = int(change_to_num(nlist[i]))
        sql1 = "insert into j(neednum,pubtime) values('%d','%s')" % (number, tlist[i])
        print(sql1)
        db.execute(sql1)
        con.commit()
    db.close()
    con.close()
    sql = "select pubtime,sum(neednum) as sum from j group by pubtime "
    df = pd.read_sql_query(sql, com)
    tlist = df["pubtime"]  # 定义两个列表
    nlist = df["sum"]
    d = dict(zip(tlist, nlist))
    x = ["1月", "2月", "3月", "4月", "5月", "6月"]  # 月份
    y = [0, 0, 0, 0, 0, 0]  # 需求人数
    for i in d.items():
        year = i[0].split("/")[0]
        print(i[0])
        mon = i[0].split("/")[1]
        if (("1" in mon) and (year == "2019")):
            y[0] = y[0] + i[1]
        elif (("2" in mon) and (year == "2019")):
            y[1] = y[1] + i[1]
        if (("3" in mon) and (year == "2019")):
            y[2] = y[2] + i[1]
        if (("4" in mon) and (year == "2019")):
            y[3] = y[3] + i[1]
        if (("5" in mon) and (year == "2019")):
            y[4] = y[4] + i[1]
        if (("6" in mon) and (year == "2019")):
            y[5] = y[5] + i[1]
    plt.figure(figsize=(8, 7), facecolor="#F1F5FB", dpi=80)
    plt.plot(x, y, color='coral')
    plt.xlabel("月份", fontsize=14)
    plt.ylabel("需求人数", fontsize=14)
    x_major_locator = MultipleLocator(1)  # 把x轴的刻度间隔设置为1，并存在变量里
    y_major_locator = MultipleLocator(50)  # 把y轴的刻度间隔设置为10，并存在变量里
    ax = plt.gca()
    # ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    # 把x轴的主刻度设置为1的倍数
    ax.yaxis.set_major_locator(y_major_locator)
    # 把y轴的主刻度设置为10的倍数
    plt.xlim(-0.5, len(x))
    # 把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
    plt.ylim(0, max(y) + 5)
    # 把y轴的刻度范围设置为0到70，同理，-5不会标出来，但是能看到一点空白
    plt.xticks(rotation=90)

    temp = zip(x, y)
    for x, y in temp:
        plt.text(x, y + 2, y, ha="center", va="top")
    if jj == "Rjob":
        j = "人工智能"
    elif jj == "Djob":
        j = "大数据"
    elif jj == "Jjob":
        j = "嵌入式"
    elif jj == "Pjob":
        j = "Python"
    plt.title("{}2019年上半年每月需求人数折线图".format(j), fontsize=14)
    plt.savefig("c.png")
    return plt
