import pymysql
def de(c):
    con = pymysql.connect("localhost", "root", "root", "sx", charset='utf8')  # 链接
    db = con.cursor()
    s="DELETE FROM message WHERE messageid={}"
    sql=s.format(c)
    db.execute(sql)
    con.commit()