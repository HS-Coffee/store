a=[1,5,21,30,15,9,30,24]
count = 0#循环次数
Sum = 0
while count<len(a):#循环a次
    #遍历的数值除5，强制整型
    num=a[count]/5
    num = int(num)
    if num*5 == a[count]:#判断强制整形后的数值乘5是否为原数值
        Sum = Sum + a[count]#如果为整形累加入变量
        print(a[count], "是5的倍数\t当前阶段和为",Sum)  # 弹出提示,"数据"是5的倍数
    else:
        print(a[count],"不是5的倍数")#弹出提示,"数据"不是5的倍数
    count = count + 1
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("遍历结束,是5倍数的总和为",Sum)