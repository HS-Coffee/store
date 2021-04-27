import random
num = random.randint(0,101)
count = 200
nub = 0
cost = 0

chose = 0
print("游戏开始\t\t剩余金币:",count,"只有7次机会哦")
while True:
    if count <= 0 or cost>7:
        print("失败~\t\t金币数:",count,"\t\t花费次数:",cost)
        break
    else:
        nub = input("数字:")
        nub = int(nub)
        cost = cost + 1
    if nub > num and (nub-num) >=10:
        count = count - 10
        print("大了\t剩余金币",count)
    elif nub < num and (num - nub) >= 10:
        count = count - 10
        print("小了\t剩余金币",count)
    elif nub > num and (nub - num) < 10:
        count = count - 25
        print("大了,但误差较小\t剩余金币",count)
    elif nub < num and (num - nub) < 10:
        count = count - 25
        print("小了,但误差较小\t剩余金币",count)
    elif nub == num :
        print("成功")
        print("剩余金币:",count,"使用次数:",cost)
        break
    else:
        print("错误")
        break