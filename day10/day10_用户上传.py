
root = input("请输入文件完整路径:\n")
f1 = open(file=root,mode="rb")
li=root.split("\\")#[]
fname="D:\\python\\a_"+li[len(li)-1]
f2 = open(file=fname,mode="wb")

data = f1.read()
f2.write(data)
f2.close()
f1.close()