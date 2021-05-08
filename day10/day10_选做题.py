#检索文件返回用户列表
def serch():
    ur = open(file="Name.txt", mode="r+", encoding="utf-8")
    data = ur.readlines()
    users = []
    for i in data:
        users.append(i.replace("\n","").split(","))
    ur.close()
    return users

#登录模块
def login():
    while True:
        user = input("\t请输入用户名,或输入q键返回:")
        if user == "q":
            break
        password = input("\t\t请输入密码:")
        info = login_logic(user,password)
        if info ==1 :
            print("登陆成功,欢迎回来")
            pass
        elif info ==2 :
            print("登陆失败,请检查用户名和密码")

#登录逻辑模块
def login_logic(user,password):
    users = serch()
    info = 0
    for t, i in enumerate(users) :
        if user == i[0] and password == i[1]:
            return 1
    else:
        return 2

#注册模块
def sigin():
    user = input("请输入用户名,或输入q返回")
    if user == "q" :
        break
    password = input("请输入密码")
    sex = input("请输入性别")
    age = input("请输入年龄")
    address = input("请输入地址")
    image = input("请输入照片完整路径")
    info = sigin_logic(user,password,sex,age,address,image)
    if info == 1:
        print("创建成功")
    elif info ==2 :
        print("用户名重复,请重新选择")

#注册逻辑模块
def sigin_logic(user,password,sex,age,address,image):
    inp = [user,password,sex,age,address,image]
    users = serch()
    info = 0
    for i in users :
        if user == i[0]:
            #用户名重复
            info = 1
            return 2
    if info == 0:
        uw = open(file="Name.txt", mode="a", encoding="utf-8")
        uw.write("\n")
        for i in inp:
            uw.write(i+",")
        uw.close()
        ir = open(file=image, mode="rb")
        li = image.split("\\")  # []
        iw = open(file="D:\\picture\\" + li[len(li) - 1], mode="wb")
        data = ir.read()
        iw.write(data)
        iw.close()
        ir.close()
        return 1

#修改模块
def change():
    user = input("请输入用户名，或输入q结束")
    if user == "q":
        return
    old_pw = input("请输入原密码")
    new_pw = input("请输入新密码")
    doublecheck = input("请再次输入新密码")
    if new_pw == doublecheck:
        info = change_logic(user,old_pw,new_pw)
        if info == 1:
            print("修改成功")
        elif info == 2:
            print("用户不存在")
        elif info ==3:
            print("用户名对应密码错误")
    else :
        print("新密码两次验证需一致")

#修改逻辑模块
def change_logic(user,old_pw,new_pw):
    users = serch()
    info = 0
    for t, i in enumerate(users) :
        if user == i[0] and old_pw == i[1] :
            i[1] = new_pw
            uw = open(file="Name.txt", mode="w+", encoding="utf-8")
            for i in users :
                for a in i :
                    uw.write(a + ",")
                uw.write("\n")
            uw.close()
            return 1
        if user == i[0] and old_pw != i[1]:
            return 3
    else :
        return 2

#退出
def exit():
    quit("吃饱喝好 一路走好")

while True:


    todo = input("欢迎来到系统\n\t选择您的业务\n\t1.登陆\n\t2.注册\n\t3.修改密码\n\t4.退出\n")
    if todo == "1":
        login()
    elif todo == "2":
        sigin()
    elif todo == "3":
        change()
    elif todo == "4":
        exit()
    else:
        print("输入有误")