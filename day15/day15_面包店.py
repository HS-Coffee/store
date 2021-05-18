import time
import threading

ti = 0
num1 = 0
case = 0

class Clock(threading.Thread):

    def run(self) -> None:
        global ti
        while True:
            if ti <=300:
                time.sleep(1)
                ti = ti + 1
                print(ti)
                # return ti
            else:
                break

class man:
    na = None
    # def __init__(self,na):
    #     self.na = na
class Cooker(threading.Thread,man):


    def run(self) -> None:
        global case
        global num1
        while ti< 300:
            while case <=300:
                case = case +1
                num1 = num1+1
                # print(self.na,":做好了一个面包!")

            else:
                # print(self.na, ":篮子满了,歇会")
                time.sleep(3)
        self.show()
    def show(self):
        show = str(self.na)+":完事了总共面包:"+str(num1)
        print(show)

class Customer(threading.Thread,man):
    num2 = 0
    def run(self) -> None:
        global case
        global num2
        while ti < 300:
            while case > 0:
                case = case -1
                self.num2 = self.num2 + 1
                # print(self.na,":买了一个面包")
            # else:
            #     # print(self.na,":篮子是空的...")
        self.show()
    def show(self):
        show = str(self.na)+":买了"+str(self.num2)+"个面包,花了:"+str(self.num2*10)+"元."
        print(show)

k1 = Cooker()
k1.na = "老赵"
k2 = Cooker()
k2.na = "老钱"
k3 = Cooker()
k3.na = "老孙"
k4 = Cooker()
k4.na = "老李"
k5 = Cooker()
k5.na = "老周"
k6 = Cooker()
k6.na = "老吴"

c1 = Customer()
c1.na = "嘉辉"
c2 = Customer()
c2.na = "雯雯"
c3 = Customer()
c3.na = "陈达"
c4 = Customer()
c4.na = "天宇"
c5 = Customer()
c5.na = "天凯"
t = Clock()

t.start()
k1.start()
k2.start()
k3.start()
k4.start()
k5.start()
k6.start()

c1.start()
c2.start()
c3.start()
c4.start()
c5.start()