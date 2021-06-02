from ddt import ddt
from ddt import data
from ddt import unpack
from selenium import webdriver
import unittest
from Test_data import test_data
from Logic import LoginPage
import time

@ddt
class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.jasonisoft.cn:8080/HKR")

    def tearDown(self) -> None:
        self.driver.quit()


    @data(*test_data.success_data)
    def test_success_login(self,testdata):
        login = LoginPage(self.driver)
        login.login(testdata["username"],testdata["password"])
        info = login.get_title()
        hope = testdata["hope"]
        self.assertEqual(hope,info)

    @data(*test_data.password_err_data)
    def test_fail_password_login(self, testdata):
        login = LoginPage(self.driver)
        login.login(testdata["username"], testdata["password"])
        info = login.get_title()
        hope = testdata["hope"]
        self.assertEqual(hope, info)

    @data(*test_data.username_err_data)
    def test_fail_username_login(self,testdata):
        login = LoginPage(self.driver)
        login.login(testdata["username"], testdata["password"])
        info = login.get_title()
        hope = testdata["hope"]
        self.assertEqual(hope, info)

    @data(*test_data.bost_err_data)
    def test_fail_bost_login(self,testdata):
        login = LoginPage(self.driver)
        login.login(testdata["username"], testdata["password"])
        info = login.get_title()
        hope = testdata["hope"]
        self.assertEqual(hope, info)