#界面打印类
class Show:

    #主界面打印
    def Menu(self):
        info = '''* * * * * * * * * * * * * * * * *
*\t\t\t中国工商银行\t\t\t*
*\t\t\t账户管理系统\t\t\t*
*\t\t\t\tV3.0\t\t\t*
* * * * * * * * * * * * * * * * *
*\t1.开户\t\t\t\t\t\t*
*\t2.存钱\t\t\t\t\t\t*
*\t3.取钱\t\t\t\t\t\t*
*\t4.转账\t\t\t\t\t\t*
*\t5.查询\t\t\t\t\t\t*
*\t6.Bye!\t\t\t\t\t\t*
* * * * * * * * * * * * * * * * *'''
        print(info)
    #新增用户打印
    def Newuser(self,account,username,password,country,province,street,door):
        info = '''\n\n\n开户成功:
* * * * * * * 个人信息 * * * * * *
用户ID：%s
用户名：%s
密码：%s
地址：%s-%s-%s-%s
开户行：中国工商银行-昌平支行
* * * * * * * * * * * * * * * * *
'''
        print(info % (account, username, password, country, province, street, door))
        input("按下回车键继续执行")