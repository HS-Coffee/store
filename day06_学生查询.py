students = [
    {'name':'张三','age':23,'score':88,'tel':'23423532','gender':'男'},
    {'name':'李四','age':26,'score':80,'tel':'12533453','gender':'女'},
    {'name':'王五','age':15,'score':58,'tel':'56453453','gender':'男'},
    {'name':'赵六','age':16,'score':57,'tel':'86786785','gender':'保密'},
    {'name':'小明','age':18,'score':98,'tel':'23434656','gender':'女'},
    {'name':'小红','age':23,'score':72,'tel':'67867868','gender':'女'},
]
print("\n1)	统计不及格学生的个数")
num=0
for i,n in enumerate(students):
    score = students[i]["score"]
    if score <60:
        num=num+1
print(num)
print("\n2)	统计未成年学生的个数")
num=0
for i,n in enumerate(students):
    age = students[i]["age"]
    if age <18:
        num=num+1
print(num)
print("\n3)	打印手机尾号是8的学生的名字")
for i,n in enumerate(students):
    tel = students[i]["tel"]
    if tel.endswith("8"):
        print(students[i])

print("\n4)	打印最高分和对应的学生的名字")
Max = 0
MaxName = ""
Min = 100
MinName = ""
for i,n in enumerate(students[i]):
    if students[i]["score"]>Max:
        Max=students[i]["score"]
        MaxName = students[i]["name"]
    if students[i]["score"]<Min:
        Min = students[i]["score"]
        MinName = students[i]["name"]
print("最高:",MaxName,"最低:",MinName)

print("\n5)	将列表按学生成绩从大到小排序")
dic = {}
for i in students:
    dic[i["name"]]=[i["score"]]
data = sorted(dic.items(),key=lambda x:x[1],reverse= True)
print(data)

print("\n6)	删除性别保密的所有学生")
for i,n in enumerate(students):
    if students[i]["gender"]=="保密":
        del students[i]
for i in students:
    print(i)