import unittest
from User import User
from Address import Address
from Logic_bank import Logic
from DBUtils import DBTools

class TestQunqian(unittest.TestCase):
    #初始化

    def setUp(self) -> None:
        self.ur = User()
        self.ad = Address()
        self.dbu = DBTools()
        self.logic = Logic()
    def Test(self):
        info = self.logic.quQian(self.ur)
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

    #正常取钱
    def test_Quqian1(self):
        self.newUser()

        inf = 0
        self.ur.setMoney(1)
        info = self.Test()
        self.assertEqual(inf,info)

    #用户不正确密码正确
    def test_Quqian2(self):
        self.newUser()

        inf = 1
        self.ur.setAccount("22222222")
        self.ur.setMoney(1)
        info = self.Test()
        self.assertEqual(inf,info)

    #用户正确密码不正确
    def test_Quqian3(self):
        self.newUser()

        inf = 2
        self.ur.setPassword("222222")
        self.ur.setMoney(1)
        info = self.Test()
        self.assertEqual(inf,info)

    #用户密码皆不正确
    def test_Quqian4(self):
        self.newUser()

        inf = 1
        self.ur.setAccount("00000000")
        self.ur.setPassword("0000000")
        self.ur.setMoney(1)
        info = self.Test()
        self.assertEqual(inf,info)

    #边界值999
    def test_Quqian5(self):
        self.newUser()

        inf = 0
        self.ur.setMoney(999)
        info = self.Test()
        self.assertEqual(inf,info)
    #边界值1000
    def test_Quqian6(self) :
        self.newUser()

        inf = 0
        self.ur.setMoney(1000)
        info = self.Test()
        self.assertEqual(inf, info)
    # 边界值1
    def test_Quqian7(self) :
        self.newUser()

        inf = 0
        self.ur.setMoney(1)
        info = self.Test()
        self.assertEqual(inf, info)
    # 边界值0
    def test_Quqian8(self) :
        self.newUser()

        inf = 3
        self.ur.setMoney(0)
        info = self.Test()
        self.assertEqual(inf, info)
    # 边界值-1
    def test_Quqian9(self) :
        self.newUser()

        inf = 3
        self.ur.setMoney(-1)
        info = self.Test()
        self.assertEqual(inf, info)
    # 边界值1001
    def test_Quqian10(self) :
        self.newUser()

        inf = 3
        self.ur.setMoney(1001)
        info = self.Test()
        self.assertEqual(inf, info)