import unittest
from User import User
from Address import Address
from Logic_bank import Logic
from DBUtils import DBTools

class TestCunqian(unittest.TestCase):
    #初始化

    def setUp(self) -> None:
        self.ur = User()
        self.ad = Address()
        self.dbu = DBTools()
        self.logic = Logic()

    def newUser(self):
        self.ur.setAccount("11111111")
        self.ur.setUsername("111")
        self.ur.setPassword("111111")
        self.ur.setMoney(0)
        self.ur.setAddress(self.ad)
        self.ad.setCountry("中国")
        self.ad.setProvince("山东省青岛市")
        self.ad.setStreet("市北区错埠龄二路")
        self.ad.setDoor("一单元401户")
        self.logic.xinZeng(self.ur, self.ad)

    def test_Cunqian1(self):
        inf = True
        self.newUser()

        self.ur.setAccount("11111111")
        self.ur.setMoney(100)
        info = self.logic.cunQian(self.ur)

        self.dbu.update("DELETE FROM bank", [])
        self.assertEqual(inf,info)

    def test_Cunqian2(self):
        inf = False
        self.newUser()

        self.ur.setAccount("22222222")
        self.ur.setMoney(100)
        info = self.logic.cunQian(self.ur)
        self.dbu.update("DELETE FROM bank",[])
        self.assertEqual(inf,info)

