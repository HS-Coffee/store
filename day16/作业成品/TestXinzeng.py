import unittest
from User import User
from Address import Address
from Logic_bank import Logic
from DBUtils import DBTools

class TestXinzeng(unittest.TestCase):

    def setUp(self) -> None:
        self.ur = User()
        self.ad = Address()
        self.dbu = DBTools()
        self.logic = Logic()
    # 正常添加 返回值1
    def test_Xinzeng1(self):
        inf =1
        self.ur.setAccount("11111111")
        self.ur.setUsername("111")
        self.ur.setPassword("111111")
        self.ur.setMoney(0)
        self.ur.setAddress(self.ad)
        self.ad.setCountry("中国")
        self.ad.setProvince("山东省青岛市")
        self.ad.setStreet("市北区错埠龄二路")
        self.ad.setDoor("一单元401户")
        info = self.logic.xinZeng(self.ur,self.ad)
        self.dbu.update("DELETE FROM bank",[])
        self.assertEqual(inf,info)
    # 重复添加 返回值2
    def test_Xinzeng2(self) :
        inf = 2
        self.ur.setAccount("22222222")
        self.ur.setUsername("111")
        self.ur.setPassword("111111")
        self.ur.setMoney(0)
        self.ur.setAddress(self.ad)
        self.ad.setCountry("中国")
        self.ad.setProvince("山东省青岛市")
        self.ad.setStreet("市北区错埠龄二路")
        self.ad.setDoor("一单元401户")
        info = self.logic.xinZeng(self.ur,self.ad)
        self.ur.setAccount("22222222")
        self.ur.setUsername("111")
        self.ur.setPassword("111111")
        self.ur.setMoney(0)
        self.ur.setAddress(self.ad)
        self.ad.setCountry("中国")
        self.ad.setProvince("山东省青岛市")
        self.ad.setStreet("市北区错埠龄二路")
        self.ad.setDoor("一单元401户")
        info = self.logic.xinZeng(self.ur,self.ad)
        self.dbu.update("DELETE FROM bank",[])
        self.assertEqual(inf, info)
    # 超过范围? 返回值3t
    # 复制一百条记录么?
    def test_Xinzeng3(self):
        inf = 1
        for i in range(100):
            self.ur.setAccount(str(i))
            self.ur.setUsername(str(i))
            self.ur.setPassword("111111")
            self.ur.setMoney(0)
            self.ur.setAddress(self.ad)
            self.ad.setCountry(str(i))
            self.ad.setProvince(str(i+1))
            self.ad.setStreet(str(i+2))
            self.ad.setDoor(str(i+3))
            info = self.logic.xinZeng(self.ur,self.ad)
        self.dbu.update("DELETE FROM bank",[])
        self.assertEqual(inf, info)
    def test_Xinzeng4(self):
        inf = 1
        for i in range(99):
            self.ur.setAccount(str(i))
            self.ur.setUsername(str(i))
            self.ur.setPassword("111111")
            self.ur.setMoney(0)
            self.ur.setAddress(self.ad)
            self.ad.setCountry(str(i))
            self.ad.setProvince(str(i+1))
            self.ad.setStreet(str(i+2))
            self.ad.setDoor(str(i+3))
            info = self.logic.xinZeng(self.ur,self.ad)
        self.dbu.update("DELETE FROM bank",[])
        self.assertEqual(inf, info)

    def test_Xinzeng5(self) :
        inf = 3
        for i in range(101) :
            self.ur.setAccount(str(i))
            self.ur.setUsername(str(i))
            self.ur.setPassword("111111")
            self.ur.setMoney(0)
            self.ur.setAddress(self.ad)
            self.ad.setCountry(str(i))
            self.ad.setProvince(str(i + 1))
            self.ad.setStreet(str(i + 2))
            self.ad.setDoor(str(i + 3))
            info = self.logic.xinZeng(self.ur,self.ad)
        self.dbu.update("DELETE FROM bank",[])
        self.assertEqual(inf, info)