a1=0
a2=0
r1=0
ALL=0
MAX=0
MID=0

while r1<10:
    r1 = r1 + 1
    print("第",r1,"次循环")
    a1 = input("输入数量:")
    a1 = int(a1)
    ALL= ALL+a1
    MID= ALL/r1
    if a1 > MAX:
        MAX = a1
    print("当前阶段总计",ALL,"\t当前阶段平均",MID,"\t当前阶段最大为",MAX)
print("-_-_-_-_-_-_-结束_-_-_-_-_-_-_-_-_-")
print("总计",ALL,"\t平均",MID,"\t最大值",MAX)