import datetime
def  change_to_date(d):
    cur = datetime.datetime.now()
    if ("小时前" in d ):
        d=str(cur.year)+"/"+str(cur.month)+"/"+str(cur.day)
        #date = datetime.datetime.strftime(t,'%Y-%m-%d').date()
    elif ("昨天" in d):
        d = str(cur.year) + "/" + str(cur.month) + "/" + str(cur.day-1)
        #date = datetime.datetime.strftime(t, '%Y-%m-%d').date()
    elif "前天" in d :
        d = str(cur.year) + "/" + str(cur.month) + "/" + str(cur.day - 2)
    else:
        ti=d.split('-')
        d=ti[0]+"/"+ti[1]+"/"+ti[2]
    return d


