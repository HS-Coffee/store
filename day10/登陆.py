'''
    有一个用户数据库文件：存储所有用户的信息
    登陆：
        需求：登陆的校验必须通过文件来进行校验
'''
# 1. 将文件的所有数据读到缓存区里
users = [
]

# 读取
f = open(file="../../狼腾资料/python自动化测试/Project_Doc/day10/代码/day10/用户.txt", mode="r+", encoding="utf-8")
data = f.readlines()
for i in data:
    da = i.replace("\n","").split(",") # ["jason","admin","56","男"]
    users.append(da)
while True:
    name = input("请输入用户名：")
    password = input("请输入您的密码：")
    # 跟缓存区校验
    a = 0
    for i in users:
        if name == i[0] and password  == i[1]:
            a = 1
            break
    if a == 1:
        print("登陆成功！")
    elif a == 0:
        print("登陆失败！")


















