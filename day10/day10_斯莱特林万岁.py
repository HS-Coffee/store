f1 = open(file="scores.txt",mode="r+",encoding="utf-8")
scores = []
score = []
data = f1.readlines()
for i in data:
    score.append(i.replace("\n","").split(" "))
for t,i in enumerate(score):
    print(i[0])
    del i[0]
    for c,d in enumerate(i):
        i[c] = int(d)
    print(sum(i),"\n")
f1.close()