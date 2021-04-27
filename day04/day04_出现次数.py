List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
count1 = 0

while count1<len(List):

    count2 = 0
    List2 = []
    while count2<len(List):
        if List[count1] == List[count2]:
            List2.insert(count2,List[count2])
            #print("count1",List[count1],"和count2",List[count2],"相等")
        #else:
            #print(List[count1],List[count2], "不相等")
        count2=count2+1
    print("循环第",count1+1,"次,遍历完成",List[count1],"出现了",len(List2),"次")
    count1=count1+1