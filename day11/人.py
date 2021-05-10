'''
    人：
        姓名，年龄，性别
        吃，喝，睡觉，玩游戏
    面向对象：
        特性：封装、继承、多态（一种事务，多种形态）
        封装：
            1.将属性全部对外隐藏
                将属性前面加：__
            2.提供方法，间接能对属性进行赋值
                提供setxxx/getxxx用于赋值和获取值
'''

class User:
    __name = ""
    __age = 0
    __sex = ""

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self,age):
        if age <= 0:
            print("年龄非法！别瞎弄！")
        else:
            self.__age = int(age)

    def getAge(self):
        return self.__age

    def setSex(self,sex):
        self.__sex = sex

    def getSex(self):
        return self.__sex

    def eat(self,eatname):
        print(self.__name , "在食堂吃",eatname)

    def drink(self,dname):
        print(self.__name,"正在喝点",dname)

    def sleep(self,hour):
        print(self.__name,"已经睡了",hour,"小时！")

    def palyGame(self,gameName):
        print(self.__name,"正在玩",gameName)

    def show(self): # 展示自我
        print("我是",self.__name,"，我今年",self.__age,"岁,我是",self.__sex,"性！")

u = User()
u.setName("砸砸辉")
u.setSex("男")
u.setAge(5.6)

u.show()

