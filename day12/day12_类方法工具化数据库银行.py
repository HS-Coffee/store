from InputHelper import  InputHelper
from Logic_bank import Logic
from DBUtils import DBTools
from User import User
from Address import Address
from Show import Show

ur = User()
ad = Address()
ur.setAddress(ad)
ih = InputHelper()
logic = Logic()
db = DBTools()
show = Show()

#入口方法
def Start():

    #返回值重置
    rt = None
    #死循环
    while True :
        #打印菜单
        show.Menu()
        todo = input(":")
        if todo == "1" :
            print("\n\t开户")
            Xinzeng()
        elif todo == "2" :
            print("\n\t存钱")
            Cunqian()
        elif todo == "3" :
            print("\n\t取钱")
            Quqian()
        elif todo == "4" :
            print("\n\t转账")
            Zhuanzhang()
        elif todo == "5" :
            print("\n\t查询")
            Chaxun()
        elif todo == "6" :
            Tuichu()
        else :
            input("输入有误,回车继续")


#新增方法
def Xinzeng():
    account = ih.randomAccount()
    ur.setAccount(account)
    print("您的账号为:",account)
    ur.setUsername(ih.userHelper("用户名"))
    ur.setPassword(ih.userHelper("密码"))
    print("以下内容为地址信息:")
    ad.setCountry(ih.userHelper("国家"))
    ad.setProvince(ih.userHelper("省份"))
    ad.setStreet(ih.userHelper("街道"))
    ad.setDoor(ih.userHelper("门牌"))
    rt = logic.xinZeng(ur.getAccount(),ur.getUsername(),ur.getPassword(),
                         ad.getCountry(),ad.getProvince(),ad.getStreet(),ad.getDoor())
    if rt == 1:
        print("创建成功")
        show.Newuser(ur.getAccount(),ur.getUsername(),ur.getPassword(),
                         ad.getCountry(),ad.getProvince(),ad.getStreet(),ad.getDoor())

    elif rt == 3 :
        print("你的人口满啦,赶紧补房子吧!")
    elif rt == 2:
        print("哦,已经有个可怜虫和你重名了~")
    elif rt == 4:
        print("未知错误!")

#存钱方法
def Cunqian():
    ur.setAccount(ih.userHelper("账号"))
    ur.setMoney(ih.userHelper("存入金额"))

    rt = logic.cunQian(ur.getAccount(),ur.getMoney())
    if rt == True:
        print("\n\n成功存入金额",ur.getMoney())
    else:
        print("不存在的用户!")
    input("按下回车继续")
#取钱方法
def Quqian():
    ur.setAccount(ih.userHelper("账号"))
    ur.setPassword(ih.userHelper("密码"))
    ur.setMoney(ih.userHelper("取款金额"))

    rt = logic.quQian(ur.getAccount(),ur.getPassword(),ur.getMoney())
    if rt == 1:
        print("用户不存在")

    elif rt == 2:
        print("密码不正确")
    elif rt == 3 :
        print("余额不足")
    elif rt == 0:
        print("取款成功, -",ur.getMoney())
    else :
        print("未知错误")
    input("按下回车继续")

#转账方法
def Zhuanzhang():
    ur2 = User()
    ur.setAccount(ih.userHelper("转出账号"))
    ur.setPassword(ih.userHelper("该账号密码"))
    ur2.setAccount(ih.userHelper("对方账号"))
    ur.setMoney(ih.userHelper("汇款金额"))
    rt = logic.zhuanZhang(ur.getAccount(),ur.getPassword(),ur2.getAccount(),ur.getMoney())
    if rt == 1 :
        print("您的帐号或对方帐号不存在")
    elif rt == 2 :
        print("您的密码不正确")
    elif rt == 3 :
        print("金额不足")
    elif rt == 0 :
        print("转账成功,-", ur.getMoney())
    input("按下回车继续")
#查询方法
def Chaxun():
    ur.setAccount(ih.userHelper("查询帐号"))
    ur.setPassword(ih.userHelper("帐号密码"))
    sql = "select * from bank where account = %s and password = %s"
    parame = [ur.getAccount(), ur.getPassword()]
    users = db.select(sql, parame)
    if len(users) != 0 :
        print("* * * * * * * * * * * * * * * * *")
        print("当前帐号:", users[0][0], ",用户名:", users[0][1], ", 密码:", users[0][2], ", 余额:", users[0][7], "元, 用户居住地址:",
              users[0][3] + users[0][4] + users[0][5] + users[0][6],
              ", 当前开户行为:", users[0][8])  # (())
        print("* * * * * * * * * * * * * * * * *")
    else :
        print("帐号或密码错误")
    input("按下回车继续")
#退出
def Tuichu():
    db.shutdown()
    quit("吃饱喝好,一路走好!")




Start()