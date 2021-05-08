f1 = open(file="setu.jpg",mode="rb")
f2 = open(file="D:\python\setu_copy.jpg",mode="wb")

data = f1.read()
f2.write(data)
f2.close()
f1.close()