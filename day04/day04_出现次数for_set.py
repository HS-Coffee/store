List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
for i in range(len(List)):
    Time=List.count(i)
    if Time != 0:
        print(List[i],"出现的次数为:",Time,"次")