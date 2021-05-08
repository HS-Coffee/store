'''
    先读后写：
    r+,w+
'''
f1 = open(file="../../狼腾资料/python自动化测试/Project_Doc/day10/代码/day10/古诗.txt", mode="r+", encoding="utf-8")
f2 = open(file="../../狼腾资料/python自动化测试/Project_Doc/day10/代码/day10/b.txt", mode="w+", encoding="utf-8")

data = f1.read()
f2.write(data)

f2.close()
f1.close()






