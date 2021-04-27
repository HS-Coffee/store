
a=int(input("第一条边:"))

b=int(input("第二条边:"))

c=int(input("第三条边:"))
print(a,b,c)

if a+b>c and a+c>b and b+c>a:
    print("可以构成三角形")
    if a==b or a==c or c==b :
        print("且该三角形为等腰三角")
        if a==b==c :
            print("中的等边三角")
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print("且该三角为直角三角")
    else:
        print("可普通三角形")
else:
    print("错误,无法构成三角形")