class 空调类():
    __品牌 = ""
    __价格 = ""
    def getPP(self):
        return self.__品牌
    def setPP(self,品牌):
        self.__品牌 = 品牌

    def getJG(self):
        return self.__价格
    def setJG(self,价格):
        self.__价格 = 价格
    def powerOn(self):
        print("空调开机了")
    def setTime(self,时间):
        if 时间<=0:
            print("太短")
        else:
            print("空调将在",时间,"分钟后自动关闭...")
    def 空调(self,品牌,价格,时间):
        空调类.setPP(self,品牌)
        空调类.setJG(self,价格)
        空调类.setTime(self,时间)
        print("品牌:",空调类.getPP(self),"\n价格:",空调类.getJG(self))
class 测试类():
    def 测试(self):
        c = 空调类()
        c.powerOn()
        while True:
            时间 = input("请输入Time参数")
            if 时间.isdigit():
                时间 = int(时间)
                break
        品牌 = input("请输入品牌")
        价格 = input("请输入金额")

        c.空调(品牌,价格,时间)

a = 测试类()
a.测试()

