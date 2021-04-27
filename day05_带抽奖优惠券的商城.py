import random
shop=[
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
point=0
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
r=random.randint(0,1)
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
    for index,value in enumerate(shop):#打印价格表
        print(index+1,".\t",value)
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    while True:
        c = 0
        d = 0
        nub = input("请输入序号,或输入q退出")
        num = input("请输入数量")
        if nub=="Q" or nub == "q" :
            print("您的本次余额为:",salary,"\n\t积分为:",point)
            quit("欢迎下次光临")
        elif nub.isdigit() and num.isdigit() :
            nub = int(nub)
            num = int(num)
            break
        else:
            print("\n\n输入有误,重新输入")
    if nub <=len(shop) :
        if salary >= shop[nub-1][2]*num:
            for a, b in enumerate(yiyou):
                print(a, b)
                while c < len(yiyou[a]):
                    if yiyou[a][c] == "003":
                        #print("出现在", a + 1, "排,", c + 1, "列")
                        d = 1
                        break
                    elif yiyou[a][c] == "011":
                        #print("出现在", a + 1, "排,", c + 1, "列")
                        d = 2
                        break
                    c=c+1

            if d == 1 :
                print("检测到辣条优惠券")
                if shop[nub-1][2]*num>=600:
                    salary = salary - shop[nub-1][2] * num + 300
                    point = point + (shop[nub-1][2] * num - 300)//10
                    print("购买完成,已自动使用优惠券:辣条满600-300,本次消费:",shop[nub-1][2]*num-300,"\t您的当前余额为:",salary,"\t积分累计为:",point)
                    del yiyou[a]
                    print(yiyou)
            elif d == 2:
                print("检测到联想电脑优惠券")
                salary = salary - shop[nub-1][2] * num * 0.5
                point = point + (shop[nub-1][2] * num * 0.5)//10
                print("购买完成,已自动使用优惠券:联想电脑半价,本次消费:", shop[nub-1][2] * num * 0.5, "\t您的当前余额为:", salary,"\t积分累计为:",point)
                del yiyou[a]
                print(yiyou)
            else:
                print("无优惠券")
                salary = salary - shop[nub-1][2]*num
                point = point + (shop[nub-1][2] * num )//10
                print("购买完成,本次消费:",shop[nub-1][2]*num,"\t您当前余额为:",salary,"\t积分累计为:",point)
        else:
            print("余额不足~穷鬼~你需要",shop[nub-1][2]*num,"\t而你只有\n")

    else:
        print("商品不存在")