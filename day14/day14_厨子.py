class Cooker:
    __Name = ""
    __age  = 0

    def getName(self):
        return self.__Name
    def setName(self,name):
        self.__Name = name
    def getAge(self):
        return self.__age
    def setAge(self,age):
        self.__age = age
    def 煮饭(self):
        pass
class Cooker2(Cooker):
    def 炒菜(self):
        pass

class Cooker3(Cooker2):
    def 煮饭(self):
        print("我是饭堂大师傅,今年",self.getAge(),"岁,今天表演一个 无米之炊!")
    def 炒菜(self):
        print("我是饭堂大师傅",self.getName(),",今天表演一个 辣炒闻闻!")

class Test:
    def test(self):
        cooker = Cooker3()
        cooker.setAge(25)
        cooker.setName("仉嘉辉")
        cooker.煮饭()
        cooker.炒菜()
test = Test()
test.test()