int2 = 9

while int2>=1 :

    int1 = 1
    while int1<=9:
        if int1<=int2:
            print(int1,"X",int2,"=",int1*int2,"\t",end="")
        int1 = int1 +1
    print("\n")
    int2 = int2 -1