list = [1,2,3,4,5,6,7,8,9]
list2=[]
print(list2)
count = 0

while count<len(list) :
    count = count +1
    list2.insert(count,list[len(list)-count])
    print(list2)
list=list2
print("\n\n list:",list,"\nend")