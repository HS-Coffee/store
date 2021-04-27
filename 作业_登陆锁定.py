tryTime=0
userName = ""
passWord = ""
while tryTime<3:
    userName = input("请输入用户名密码")
    passWord = input("请输入用户名密码")
    tryTime = tryTime + 1
    if userName != "root" or passWord != "admin":
        print("登录失败")
        print("警告,已失败第",tryTime,"次!")
    else:
        print("登陆成功,欢迎回来.")
        break
else:
    while True:
        print("您已触发锁定条件,拒绝访问.")
print("-----------欢迎回来,指挥官.---------")