from DBUtils import shutdown
from DBUtils import select
from DBUtils import update
f = open(file="用户数据.txt",mode="r+",encoding="GBK")
data = f.readlines()
users = []
for i in data:
    users.append(i.replace("\n","").split(","))
print(users)
sql = "INSERT INTO test1 VALUES(%s,%s,%s)"
for i in users:
    print(i)
    update(sql,i)
sql = "select sum(净资产) from test1"
print(select(sql,[]))
shutdown()
f.close()