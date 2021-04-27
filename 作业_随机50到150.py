#使用random模块，如何产生 50~150之间的数？
import random
a = 0
b =0
while a != 150:
    a = random.randint(50,150)
    b = b+1
    print("本次输出结果:",a,"运行次数:",b)