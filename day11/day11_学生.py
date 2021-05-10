class 学生类():
    __姓名 = ""
    __年龄 = 0
    def setName(self,Name):
        self.__姓名 = Name
    def getName(self):
        return self.__姓名
    def setAge(self,Age):
        self.__年龄 = Age
    def getAge(self):
        return self.__年龄

    def 介绍(self):
        print("大家好，我叫",self.__姓名,"，今年",self.__年龄,"岁了！")
    def 对比(self,傻逼2):
        if self.__年龄>傻逼2:
            return "我比同桌大"+str(self.__年龄-傻逼2)+"岁！"
        elif self.__年龄<傻逼2:
            return  "我比同桌小"+str(傻逼2-self.__年龄)+"岁！"
        elif self.__年龄 == 傻逼2:
            return "我和同桌一样大！"
class 测试类():
    c1 = 学生类()
    c1.setAge(25)
    c1.setName("傻逼1")
    c2 = 学生类()
    c2.setAge(27)
    c2.setName("傻逼2")
    c1.介绍()
    c2.介绍()
    print(c2.对比(c1.getAge()))