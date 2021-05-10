class 人类():
    姓名 = ""
    性别 = ""
    年龄 = 0
    余额 = 0
    手机品牌 = ""
    电池容量 = 0
    屏幕大小 = 0
    待机时长 = 0
    积分 = 0
    def 发短信(self,要求参数):
        print(self.姓名,self.手机品牌,要求参数)
    def 打电话(self,对方号码,时间):
        if 对方号码 != "" :
            if self.余额 > 1:
                print("已接通")
                input("回车挂断")
                if 时间 > 20 :
                    时间 = 时间 - 30
                    self.余额 = self.余额 - 时间*0.65 - 20*0.8 - 10
                    self.积分 = self.积分 + 时间*48 + 20*39 + 10 * 15
                    return 时间*0.65 + 20*0.8 + 10
                elif 时间 > 10 :
                    时间 = 时间 - 10
                    self.余额 = self.余额 - 时间 * 0.8 - 10
                    self.积分 = self.积分 + 时间 * 39 + 10 * 15
                    return 时间 * 0.8 + 10
                elif 时间 > 0 :
                    self.余额 = self.余额 - 时间
                    self.积分 = self.积分 + 时间 * 15
                    return 时间
                else:
                    print("时间?")
                print("已挂断")
            else:
                return "余额不足"
        else:
            return "空号"

class test():
    人 = 人类()
    人.余额 = 100
    print(人.打电话("110",50))
    人.发短信("喇叭")