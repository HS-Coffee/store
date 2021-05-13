def shopping():
    import random#引入随机数,为随机优惠券使用
    import xlwt
    from day13_遍历工具 import tools
    wt = xlwt.Workbook()
    wts = wt.add_sheet("user")

    tool = tools()
    fname,shop = tool.rd("shop.xls","shop")
    for i in shop:
        i[2] = float(i[2])
    # shop=[#商品列表
    #     ["003","辣条",0.5],
    #     ["004","太空人果冻",0.1],
    #     ["005","肥宅",50],
    #     ["010","神舟电脑",10000],
    #     ["011","联想电脑",5000],
    #     ["012","鼠标",5],
    #     ["101","现抓刘雯雯",99999999],
    #     ["102","蔡徐坤",0.01],
    #     ["103","肖战",0.01]
    # ]
    point=round(0,0)#积分
    mycart = []
    allCost = 0.00
    cost = 0.00
    #以下是余额
    while True:
        f,users = tool.rd("shop.xls","user")
        user = input("请输入用户名")
        password = input("请输入密码")
        info = 0
        for p,i in enumerate(users):
            if user == i[0] and password == i[1]:
                salary = float(i[2])
                point = int(i[3])
                print("欢迎回来",user,"\n您的余额为:",salary,"\t积分为:",point)
                info = 1
            else:
                print("登录失败~")
        if info == 1:
                break

    #以下是优惠券
    r=0
    r=random.randint(0,1)#生成随机数
    youhui=[
        ["003",10,300],
        ["011",20,0.5]
    ]
    yiyou=[]
    if r==0:
        youhui[r][1] = youhui[r][1] - 1#减系统优惠券数量
        yiyou.append([youhui[r][0],1,youhui[r][2]])#在用户优惠券里添加
        print("获得辣条600-300优惠")
    elif r==1 :
        youhui[r][1] = youhui[r][1] - 1
        yiyou.append([youhui[r][0],1,youhui[r][2]])
        print("获得联想电脑半价券")
    else:
        print("?")
    input("请按回车继续")
    #以下是商城:
    while True:
        # 打印价格表
        for index,value in enumerate(shop):
            print(index+1,".\t",value)
        print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        #二级循环
        while True:
            #c,d为搜索优惠券结果保存
            c = 0
            d = 0
            #获取商品序号
            nub = input("请输入序号,或输入q结账,退出")
            #退出并结算
            if nub=="Q" or nub == "q" :
                # 结算-寻找优惠券：
                for a, b in enumerate(yiyou):
                    print(a, b)
                    while c < len(yiyou[a]):
                        #寻找辣条优惠券
                        if yiyou[a][c] == "003":
                            # print("出现在", a + 1, "排,", c + 1, "列")
                            d = 1
                            break
                        #寻找电脑优惠券
                        elif yiyou[a][c] == "011":
                            # print("出现在", a + 1, "排,", c + 1, "列")
                            d = 2
                            break
                        c = c + 1
                #对购物车里的内容进行查找调整消费
                if d == 1 :
                    for i,n in  enumerate(mycart):
                        if mycart[i][0]=="辣条" and mycart[i][3]>=600:
                            mycart[i][3]=mycart[i][3]-300
                            del yiyou[c]
                            print("已检测到优惠券:辣条满600-300 已自动使用")
                        else:
                            print("已检测到优惠券:辣条满600-300,但不满足条件~")
                elif d == 2 :
                    for i,n in  enumerate(mycart):
                        if mycart[i][0]=="联想电脑" :
                            mycart[i][3]=mycart[i][3]/2
                            del yiyou[c]
                            print("已检测到优惠券:联想电脑半价 已自动使用")
                            break
                        else:
                            print("已检测到优惠券:联想电脑半价,但不满足条件~")
                #计算购物车内总价
                print("以下是您购物车内的物品\n商品名\t\t单价\t数量\t单项总计")
                for i,n in enumerate(mycart):
                    print(n)
                    allCost = allCost+ mycart[i][3]

                if allCost <= salary:
                    salary = str(salary - allCost)
                    point = str(point + int(allCost//10))
                    wts.write(p,2,salary)
                    wts.write(p,3,point)
                    wt.save("shop.xls")
                    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
                    print("结账成功,您的总消费为",allCost,"\t余额",salary,"\t积分为",point)
                    allCost = 0
                    mycart=[]
                    quit("吃饱喝好,一路走好!")
                else:
                    print("结账失败,余额不足")

            num = input("请输入数量")
            #获取编号/数量添加至购物车
            if nub.isdigit() and num.isdigit() :
                nub = int(nub)-1#减1用以匹配数据位置
                num = int(num)
                #判断编号/数量是否满足条件:
                if nub>=0 and num>0 and nub <=len(shop):
                    # 添加购物车
                    for i, n in enumerate(shop):
                        if nub == i:
                            cost = shop[nub][2] * num
                            mycart.append([shop[nub][1], shop[nub][2], num, cost])
                            #allCost = allCost + cost
                            cost = 0
                    print("添加成功,当前购物车内容如下\n   物品 单价 数量 总价")
                    for i, n in enumerate(mycart):
                        print(n)
                else:
                    print("\n你在逗我?")
            else:
                print("\n输入有误,重新输入")
        else:
            print("商品不存在")
shopping()