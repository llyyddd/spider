import requests
from bs4 import BeautifulSoup
import pymysql
import  nnum
import exDate
def catch_D(jobt):
    url1="https://xiaoyuan.zhaopin.com/part/0/0_0_0_0_0_-1_{}_{}_0"
    sp=BeautifulSoup(requests.get(url1.format(jobt, 1)).text, "html.parser")
    con=pymysql.connect("localhost", "root", "root", "sx", charset='utf8')#链接
    db=con.cursor()
    if jobt=="人工智能":
        jj="Rjob"
    elif jobt=="大数据":
        jj="Djob"
    elif jobt=="嵌入式":
        jj="Jjob"
    elif jobt=="Python":
        jj="Pjob"
    s= "truncate table {}"
    sql1=s.format(jj)
    db.execute(sql1)
    con.commit()
    ptotal= sp.find("span",attrs={"class": "searchResultPagePer fr"}).get_text().split("/")[1]
    for i in range(1, int(ptotal)+1):
        print(i)
        f = requests.get(url1.format(jobt,i)).text
        soup = BeautifulSoup(f, "html.parser")
        divlist2 = soup.find_all(class_='searchResultItemDetailed')
        for div in divlist2:
            jn=div.find("a").get_text()
            city=div.find("em",attrs={"class":"searchResultJobCityval"}).get_text()
            num = div.find("p", attrs={"class": "searchResultCompanyInfodetailed"})
            jt=num.find_all("span", attrs={"class": "searchResultKeyval"})
            if (len(jt)==3):
                jobtype=jt[1].get_text().strip()[5:]
                n1=jt[2].get_text().strip()[5:]
            else:
                jobtype = jt[3].get_text().strip()[5:]
                n1 = jt[4].get_text().strip()[5:]
            #note=div.find("p", attrs={"class": "searchResultJobdescription"}).get_text().strip()[5:]
            com = div.find("p", attrs={"class": "searchResultCompanyname"}).get_text()
            cty = num.find_all("span", attrs={"class": "searchResultKeyval"})
            comty=cty[0].get_text().strip()[5:]
            d2= div.find("p", attrs={"class": "searchResultJobAdrNum"})
            dd=d2.find_all("span", attrs={"class": "searchResultKeyval"})
            d=dd[1].get_text().strip()[5:]
            pubtime = exDate.change_to_date(d)
            #neednum=nnum.change_to_num(n1)
            zhaotype = div.find("span", attrs={"class": "oTips oTips4 fl"})
            if (zhaotype != None):
                zt = zhaotype.get_text()
            else:
                z = div.find("span", attrs={"class": "oTips oTips1 fl"})
                if (z!=None):
                   zt = z.get_text()
                else:
                    zt="社会招聘"
            #print(zt)
            ss= "insert into {}(jobname,jobtype,city,neednum,company,cptype,recruittype,pubtime) values('%s','%s','%s','%s','%s','%s','%s','%s')" % (
            jn,jobtype, city, n1, com, comty, zt, pubtime)
            sql =ss.format(jj)
            db.execute(sql)
            con.commit()
    db.close()
    con.close()
    print("爬虫结束！")










