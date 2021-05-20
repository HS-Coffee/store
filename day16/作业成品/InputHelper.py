from DBUtils import  DBTools
import random

db = DBTools()

#辅助输入类
class InputHelper:

    #用户信息辅助输入
    def userHelper(self,chose,datatype = "str"):
        while True:
            print("请输入",chose,",或输入q退出")
            i = input(">")
            if i == "q":
                db.shutdown()
                quit("吃饱喝好一路走好!")
            if len(i.strip()) == 0:
                print("不能空值输入,请重新输入")
                continue
            if "密码" in chose:
                if len(i) != 6:
                    print("请输入6位密码!")
                    continue
            if "金额" in chose:
                if i.isdigit() or i =="0":
                    int(i)
                    return i
                else:
                    print("请输入正确金额!")
                    continue
            else:
                return i

    #账号随机数
    def randomAccount(self):
        li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
        while True :  # 死循环,用于检测ID是否重复
            account = ""
            for i in range(8) :  # 循环8次 #0  ~  13  5
                account = account + li[int(random.random() * len(li))]  # 随机选取内容
            sql = "select account from bank where account = %s"  # 查询语句,预留出ID位置
            parame = [account]
            users = db.select(sql,parame)  # 将查询结果装入users
            if len(users) == 0 :  # 当users中的结果为空时
                break  # 跳出循环
        return account
# ih = InputHelper()
# info = ih.userHelper("金额")
# print(info)