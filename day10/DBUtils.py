import pymysql
#声明变量:
host = "localhost"
user = "root"
password = ""
database = "day10"


con = pymysql.connect(host=host,user=user,password=password,database=database)
cursor = con.cursor()


def update(sql,param):
    num = cursor.execute(sql,param)
    con.commit()
    return num

def select(sql,param):
    cursor.execute(sql,param)
    return cursor.fetchall()

def shutdown():
    cursor.close()
    con.close()