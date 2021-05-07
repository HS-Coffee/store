import random
import pymysql

con = pymysql.connect(host="127.0.0.1",user="root",password="",database="银行")

cursor = con.cursor()




# 2.银行的名称写死
bank_name = "中国工商银行-昌平支行"
'''users={
    "张三":{"password":"000","money":10000},
    "李四":{"password":"111","money":10000},
}'''

#新增_用户端模块
def xinzeng():
    # 随机获取账号
    li = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",
          "r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
          "S","T","U","V","W","X","Y","Z"]
    while True:
        account = ""
        for i in range(8):
            index = random.randint(0, len(li) - 1)
            account = account + li[index]
        if account not in users:
            break
    print("用户信息:\n用户ID为:",account)
    username = input("请输入用户名:")
    while True:
        password = input("请输入6位密码")
        if len(password) == 6:
            break
        else:
            print("输入有误")
    print("地址信息")
    country = input("请输入国家:")
    province = input("请输入省份:")
    street = input("请输入街道:")
    door = input("请输入门牌号:")

    rt = bank_xinzeng(account,username,password,country,province,street,door)
    if rt == 1 :
        print("开户成功:")
        info = '''
        * * * * * * * 个人信息 * * * * * *
        用户ID：%s
        用户名：%s
        密码：%s
        地址：%s%s%s%s
        开户行：%s
        * * * * * * * * * * * * * * * * *
        '''
        print(info % (account,username,password,country,province,street,door,bank_name))
    elif rt == 2:
        print("用户ID重复")
    elif rt == 3:
        print("用户库已满")
    elif rt == 4:
        print("发生错误")

#新增_服务端模块
def bank_xinzeng(account,username,password,country,province,street,door):
    sql = "select account from bank"
    cursor.execute(sql)
    users = cursor.fetchall()
    if len(users) >= 100:
        return 3
    users = ()
    sql = "select account from bank where account = %s"
    parame = [account]
    cursor.execute(sql,parame)
    users = cursor.fetchall()
    if len(users) != 0:
        return 2
    else:
        users = ()
        sql = "INSERT INTO bank VALUES(%s,%s,%s,%s,%s,%s,%s,0,'中国工商银行-昌平支行');"
        param = [account,username,password,country,province,street,door]
        num = cursor.execute(sql,param)
        con.commit()
        if num >=1:
            return 1
        else:
            return 4

#存钱_用户端模块
def cunqian():
    user = input("请输入用户ID")
    money = input("请输入存入金额")
    if money.isdigit():
        money = int(money)
        rt = bank_cunqian(user,money)
        if rt == True:
            print("成功存入金额",money)
        else:
            print("不存在该用户!")

#存钱_服务端模块
def bank_cunqian(user,money):
    sql = "select account from bank where account  = %s ;"
    param = [user]
    cursor.execute(sql,param)
    users = cursor.fetchall()
    if len(users) != 0:
        sql = "UPDATE bank SET money = money + %s WHERE account = %s ;"
        parame = [money,user]
        cursor.execute(sql,parame)
        con.commit()
        return True
    else:
        return False

#取钱_用户端模块
def quqian():
    print("* * * * * * * 取钱 * * * * * * * *")
    take_user = input("请输入用户ID")
    take_password = input("请输入用户密码")
    take_money = input("请输入取钱金额")
    if take_money.isdigit():
        take_money = int(take_money)
        rt = bank_quqian(take_user,take_password,take_money)
        if rt == 1 :
            print("用户不存在")
        if rt == 2 :
            print("密码不正确")
        if rt == 3 :
            print("金额不充足")
        if rt == 0 :
            print("取钱成功.-",take_money)
    else:
        print("输入错误请检查")

#取钱_服务端模块
def bank_quqian(take_user,take_password,take_money):
    #判断 用户存在
    sql = "select account from bank where account = %s;"
    parame = [take_user]
    cursor.execute(sql,parame)
    users = cursor.fetchall()
    if len(users) != 0 :
        # 判断 密码正确
        users=()
        sql = "select account from bank where account = %s and password = %s;"
        parame = [take_user,take_password]
        cursor.execute(sql, parame)
        users = cursor.fetchall()
        if len(users) != 0 :
            #判断 余额足够
            users=()
            sql = "select account from bank where account = %s and password = %s and (money-'%s') >= 0;"
            parame = [take_user, take_password,take_money]
            cursor.execute(sql, parame)
            users = cursor.fetchall()
            if len(users) != 0:
                #满足 扣钱
                users=()
                sql = "update bank set money = money - %s where account = %s "
                parame = [take_money,take_user]
                cursor.execute(sql,parame)
                con.commit()
                return 0#成功 返回值0
            else:
                return 3#钱不够返回3
        else:
            return 2#用户密码不正确返回2
    else:
        return 1#返回1

#转账_用户端模块
def zhuanzhang():
    send_user = input("\n请输入您的ID")
    send_userPw = input("\t请输入您的密码")
    send_to = input("\t\t请输入对方ID")
    send_money = input("\n\t\t\t请输入转账金额")
    if send_money.isdigit():
        send_money = int(send_money)
        rt = bank_zhuanzhang(send_user,send_userPw,send_to,send_money)
        if rt == 1:
            print("您的帐号或对方帐号不存在")
        elif rt == 2:
            print("您的密码不正确")
        elif rt == 3:
            print("金额不足")
        elif rt == 0:
            print("转账成功,-",send_money)
    else:
        print("输入有误")

#转账_服务端模块
def bank_zhuanzhang(send_user,send_userPw,send_to,send_money):
    sql= "select account from bank where account = %s or account = %s"
    parame =[send_user,send_to]
    cursor.execute(sql,parame)
    users=cursor.fetchall()
    if len(users)==2:
        users = ()
        sql = "select account from bank where account = %s and password = %s"
        parame = [send_user, send_userPw]
        cursor.execute(sql, parame)
        users = cursor.fetchall()
        if len(users) == 1:
            users = ()
            sql = "select account from bank where account = %s and password = %s and money >= %s"
            parame = [send_user, send_userPw,send_money]
            cursor.execute(sql, parame)
            users = cursor.fetchall()
            if len(users)==1 :
                sql = "update bank set money = (money - %s) where account = %s ;"
                parame = [send_money,send_user]
                cursor.execute(sql,parame)
                sql = "update bank set money = (money + %s) where account = %s ;"
                parame = [send_money, send_to]
                cursor.execute(sql,parame)
                con.commit()
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

#查询
def chaxun():
    user = input("请输入用户ID:")
    passwd = input("请输入用户密码")
    sql = "select * from bank where account = %s and password = %s"
    parame = [user,passwd]
    cursor.execute(sql,parame)
    users = cursor.fetchall()
    if len(users)!=0:
        print("* * * * * * * * * * * * * * * * *")
        print("当前帐号:",users[0][0],",用户名:",users[0][1],", 密码:",users[0][2],", 余额:",users[0][7],"元, 用户居住地址:",
                users[0][3]+users[0][4]+users[0][5]+users[0][6],
                ", 当前开户行为:",users[0][8])  # (())
        print("* * * * * * * * * * * * * * * * *")
    else:
        print("帐号或密码错误")

#退出
def tuichu() :
    cursor.close()
    con.close()
    quit("吃饱喝好,一路走好!")
#主菜单打印
def welcome():
    info = '''* * * * * * * * * * * * * * * * *
*\t\t\t中国工商银行\t\t\t*
*\t\t\t账户管理系统\t\t\t*
*\t\t\t\tV1.0\t\t\t*
* * * * * * * * * * * * * * * * *
*\t1.开户\t\t\t\t\t\t*
*\t2.存钱\t\t\t\t\t\t*
*\t3.取钱\t\t\t\t\t\t*
*\t4.转账\t\t\t\t\t\t*
*\t5.查询\t\t\t\t\t\t*
*\t6.Bye!\t\t\t\t\t\t*
* * * * * * * * * * * * * * * * *'''
    print(info)

# #程序主体:# #
while True:
    sql = ""
    parame = []
    users = ()
    welcome()
    todo = input(":")
    print(type(todo), todo)
    if todo=="1":
        xinzeng()
    elif todo=="2":
        cunqian()
    elif todo=="3":
        quqian()
    elif todo=="4":
        zhuanzhang()
    elif todo=="5":
        chaxun()
    elif todo=="6":
        tuichu()
    else:
        print("输入有误")