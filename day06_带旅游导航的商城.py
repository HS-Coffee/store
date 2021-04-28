city={
    "北京" : {
        "昌平" : {
            "回龙观" : ["永辉", "永旺"],
            "龙泽" : ["海底捞", "呷哺呷哺"]
        },
        "海淀" : {
            "公主坟" : ["军事博物馆", "五道口切糕"],
            "香山" : ["香山", "植物园"],
            "高校" : ["清华", "北大"]
        },
        "朝阳" : {
            "朝阳南北塔" : ["世纪公园", "玉渊潭公园"],
            "双塔" : ["双塔白醋"]
        },
        "延庆" : {
            "龙庆峡" : ["龙庆峡"]
        }
    },
    "青岛" : {
        "市北" : {
            "登州路":["啤酒街","啤酒博物馆"],
            "辽宁路":["科技街","天幕城"],
            "威海路":["台东步行街","动物园"],

        },
        "市南" : {
            "香港西路":["八大关","第一海水浴场","中山公园"],
            "香港中路":["银座","万象城","青岛香格里拉","佳世客(永旺)"],
            "东海路":["五四广场","音乐广场","科技宫","雕塑园"],
            "中山路":["王姐烧烤","劈柴院","栈桥","海上皇宫"],
            "西镇":["西镇臭豆腐","西镇电烤肉","路边野馄饨"]
        },
        "李沧" : {
            "李村":["李村国贸"]
        },
        "崂山" : {
            "香港东路":["石老人海水浴场","金狮购物中心"],
            "崂山风景区":["北九水","巨峰","崂山旅游路北段","崂山旅游路南段"],
            "沙子口":["西麦窑","沙子口"],
            "仰口":["仰口沙滩"]
        },
    }
}
def shopping():
    print("欢迎进入随行商城")
    import random#引入随机数,为随机优惠券使用
    shop=[#商品列表
        ["003","辣条",0.5],
        ["004","太空人果冻",0.1],
        ["005","肥宅",50],
        ["010","神舟电脑",10000],
        ["011","联想电脑",5000],
        ["012","鼠标",5],
        ["101","现抓刘雯雯",99999999],
        ["102","蔡徐坤",0.01],
        ["103","肖战",0.01]
    ]
    point=round(0,0)#积分
    mycart = []
    allCost = 0.00
    cost = 0.00
    #以下是余额
    while True:
        salary = input("\n\n请输入钱包:")
        if salary.isdigit():
            salary = int(salary)
            break
        else:
            print("\n\n输入有误,重新输入")
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
                print("以下是您购物车内的物品")
                for i,n in enumerate(mycart):
                    print(n)
                    allCost = allCost+ mycart[i][3]
                if allCost <= salary:
                    salary = salary - allCost
                    point = point + (allCost//10)
                    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
                    print("结账成功,您的总消费为",allCost,"\t余额",salary,"\t积分为",point)
                    allCost = 0
                    mycart=[]
                    return "吃饱喝好,一路走好!"
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
def print_place(data):
    for i in data:
        print(i)


'''for i in city["青岛"] :
    print(i)'''
while True :
    print("欢迎进入景点查询系统")
    print_place(city)
    num1 = input("请输入您要去的城市>>>>:")
    if num1 in city:
        print_place(city[num1])
        num2 = input("请输入您要去的区>>>>:")
        if num2 in city[num1]:
            print_place(city[num1][num2])
            num3 = input("请输入需要去的景点>>>>:")
            if num3 in city[num1][num2]:
                print_place(city[num1][num2][num3])
                print("以上为景点,再会咯!")
                shopping()
                break
            elif num3 == "Q" or num3 == "q":
                print("再会咯!")
                break
            else:
                print("输入有误")
        elif num2 == "Q" or num2 == "q" :
            print("再会咯!")
            break
        else:
            print("输入有误")
    elif num1 == "Q" or num1 == "q" :
        print("再会咯!")
        break
    else:
        print("输入有误")