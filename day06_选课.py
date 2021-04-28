语文 = ['小明','小张','小黄','小杨']
数学 = ['小黄','小李','小王','小杨','小周']
英语 = ['小杨','小张','小吴','小冯','小周']
def bl(data):
    for i in data:
        print(i)
def time(data):
    dic = {}
    for i in data :
        dic [i] = data.count(i)
    return dic
学生 = 语文+数学+英语
print(学生)

学生 = time(学生)
print(学生)
print("1)\t总共有:",len(学生),"人")

num = 0
print("\n上一题的数据直接调用:",学生)
for i,n in enumerate(语文) :
    if n in 学生 and 学生[n]==1:
        print(n,"只报了第一门学科")
        num = num + 1
print(num,"人只报了第一门学科")

num = 0
print("\n上一题的数据直接调用:",学生)
for i,n in enumerate(学生):

    if 学生[n] == 1:
        print(n, "只报了第一门学科")
        num = num + 1
print(num,"人之报了一门")