class Oldphone:
    __clas = ""

    def setClas(self,clas):
        self.__clas = clas

    def getClas(self):
        return self.__clas

    def call(self):
        print("正在给xxx打电话...")

class Newphone(Oldphone):


    def call(self):
        print("语音拨号中...")
        super().call()

    def about(self):
        __clas = self.getClas()
        print("品牌为：",__clas,"的手机很好用...")

class Test:
    def test(self):
        new = Newphone()
        new.setClas("小米")
        new.call()
        new.about()

test = Test()
test.test()