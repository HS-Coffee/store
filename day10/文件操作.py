f = open(file="1.txt",mode="w+",encoding="utf-8")
f.write("1")
f2 = open(file="1.txt",mode="r+",encoding="utf-8")
print(f2.readline())
f2.close()
f.close()