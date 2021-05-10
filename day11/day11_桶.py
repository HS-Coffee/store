class cup:
    __高度 = 0
    __容积 = 0
    __颜色 = ""
    __材质 = ""

    def setH(self,高度):
        if 高度<0:
            print("有0高度的杯子?")
        else:
            self.__高度 = 高度
    def getH(self):
        return self.__高度
    def setR(self,容积):
        if 容积<0:
            print("您合着拿片纸来当杯子")
        else:
            self.__容积 = 容积
    def getR(self):
        return self.__容积
    def setC(self,颜色):
        self.__颜色 = 颜色
    def getC(self):
        return self.__颜色
    def setT(self,材质):
        self.__材质 = 材质
    def getT(self):
        return self.__材质
    def show(self):
        print("这个杯子高",self.__高度,",能装",self.__容积,"的液体.颜色是",self.__颜色,"的",self.__材质,"杯子.")

c = cup()
c.setC("绿色")
c.setT("304钢")
c.setH(15)
c.setR(500)


c.show()