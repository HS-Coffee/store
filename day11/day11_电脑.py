class pc:
    __屏幕 = 0
    __价格 = 0
    __cpu = ""
    __内存 = 0
    __电池 = 0

    def setSize(self,屏幕):
        if 屏幕<9:
            print("您的屏幕还能看见?")
        else:
            self.__屏幕 = 屏幕
    def getSize(self):
        return self.__屏幕
    def setPrice(self,价格):
        if 价格<=0:
            print("合着给您白送呗?")
        else:
            self.__价格 = 价格
    def getPrice(self):
        return self.__价格
    def setCPU(self,cpu):
        self.__cpu = cpu
    def getCPU(self):
        return self.__cpu
    def setRAM(self,内存):
        if 内存<=0:
            print("这存在吗,这不存在的")
        else:
            self.__内存 = 内存
    def getRAM(self):
        return self.__内存
    def setButton(self,电池):
        if 电池<0:
            print("您就是传说中的电表倒转?")
        else:
            self.__电池 = 电池
    def getButton(self):
        return self.__电池
    def show(self):
        print("这个电脑屏幕",self.__屏幕,",价格",self.__价格,"元.cpu是",self.__cpu,",内存为",self.__内存,",电池容量为",self.__电池)

    def 打字(self):
        print("这台电脑能打字,有一个",self.__屏幕,"的屏幕供你查看",self.__电池,"的电池供作断电续航")
    def 玩游戏(self):
        print("这台电脑CPU为",self.__cpu,"同时有",self.__内存,"供你使用",self.__屏幕,"的屏幕")
    def 看视频(self):
        print("这台电脑能看视频,有一个", self.__屏幕, "的屏幕供你查看", self.__电池, "的电池供作断电续航")

c = pc()
c.setCPU("Intel i5-8400")
c.setRAM(16)
c.setSize(15)
c.setButton(3200)
c.setPrice(7000)

c.show()
c.打字()
c.玩游戏()
c.看视频()