import unittest
from User import User
from Address import Address
from Logic_bank import Logic
from DBUtils import DBTools

class TestZhuanzhang(unittest.TestCase):
    #初始化

    def setUp(self) -> None:
        self.ur = User()
        self.ur2 = User()
        self.ad = Address()
        self.ad2 = Address()
        self.dbu = DBTools()
        self.logic = Logic()
    def Test(self,ur,ur2):
        info = self.logic.zhuanZhang(ur,ur2)
        self.dbu.update("DELETE FROM bank", [])
        return info
    def newUser(self):
        self.ur.setAccount("11111111")
        self.ur.setUsername("111")
        self.ur.setPassword("111111")
        self.ur.setMoney(1000)
        self.ur.setAddress(self.ad)
        self.ad.setCountry("中国")
        self.ad.setProvince("山东省青岛市")
        self.ad.setStreet("市北区错埠龄二路")
        self.ad.setDoor("一单元401户")
        self.logic.xinZeng(self.ur, self.ad)
        self.logic.cunQian(self.ur)

        self.ur2.setAccount("22222222")
        self.ur2.setUsername("222")
        self.ur2.setPassword("222222")
        self.ur2.setMoney(0)
        self.ur2.setAddress(self.ad)
        self.ad2.setCountry("中国")
        self.ad2.setProvince("北京市")
        self.ad2.setStreet("昌平区狼腾测试员")
        self.ad2.setDoor("356")
        self.logic.xinZeng(self.ur2, self.ad2)

    # 正常填入已有的信息成功转出转出金额为1, 返回值为0
    def test_Zhuanzhang1(self):
        self.newUser()
        inf =  0
        self.ur.setMoney(1)
        info = self.Test(self.ur,self.ur2)
        self.assertEqual(inf,info)

    # 转出帐号存在, 转入帐号不存在, 返回值为1
    def test_Zhuanzhang2(self):
        self.newUser()
        inf = 1

        self.ur2.setAccount("5")
        info = self.Test(self.ur, self.ur2)
        self.assertEqual(inf, info)
    # 转出账号不存在, 转入帐号不存在, 返回值1
    def test_Zhuanzhang3(self) :
        self.newUser()
        inf = 1

        self.ur.setAccount("5")
        info = self.Test(self.ur, self.ur2)
        self.assertEqual(inf, info)
    # 帐号均不存在, 返回值为1
    def test_Zhuanzhang4(self) :
        self.newUser()
        inf = 1

        self.ur.setAccount("5")
        self.ur2.setAccount("3")
        info = self.Test(self.ur, self.ur2)
        self.assertEqual(inf, info)
    # 转出帐号存在, 密码不存在, 返回值为2
    def test_Zhuanzhang5(self) :
        self.newUser()
        inf = 2

        self.ur.setPassword("5")
        info = self.Test(self.ur, self.ur2)
        self.assertEqual(inf, info)
    # 转出帐号密码均不存在, 返回值为1
    def test_Zhuanzhang6(self) :
        self.newUser()
        inf = 1

        self.ur.setAccount("5")
        self.ur.setPassword("0")
        info = self.Test(self.ur, self.ur2)
        self.assertEqual(inf, info)
    # 转出金额999, 返回值为0
    def test_Zhuanzhang7(self) :
        self.newUser()
        inf = 0

        self.ur.setMoney(999)
        info = self.Test(self.ur, self.ur2)
        self.assertEqual(inf, info)
    # 转出金额1000, 返回值为0
    def test_Zhuanzhang8(self) :
        self.newUser()
        inf = 0

        self.ur.setMoney(1000)
        info = self.Test(self.ur, self.ur2)
        self.assertEqual(inf, info)
    # 转出金额1001, 返回值为3
    def test_Zhuanzhang9(self) :
        self.newUser()
        inf = 3

        self.ur.setMoney(1001)
        info = self.Test(self.ur, self.ur2)
        self.assertEqual(inf, info)
    # 转出金额 - 1, 返回值为3
    def test_Zhuanzhang10(self) :
        self.newUser()
        inf = 3

        self.ur.setMoney(-1)
        info = self.Test(self.ur, self.ur2)
        self.assertEqual(inf, info)
    # 转出金额0, 返回值为3
    def test_Zhuanzhang11(self) :
        self.newUser()
        inf = 3

        self.ur.setMoney(0)
        info = self.Test(self.ur, self.ur2)
        self.assertEqual(inf, info)