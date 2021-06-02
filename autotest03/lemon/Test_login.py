from Login import Login
from Login_data import Test_data

from selenium import webdriver
from ddt import ddt
from ddt import data
from ddt import unpack
import time
import unittest

@ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.ningmengyun.com/")
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@class='menu-btn-login']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@class='toggle-container']").click()
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()

    @data(*Test_data.success_data)
    def test_success_login(self,testdata):
        login = Login(self.driver)
        login.login(testdata["username"],testdata["password"])
        time.sleep(3)
        real = login.get_title()
        hope = testdata["hope"]
        self.assertEqual(real,hope)

    @data(*Test_data.fail_password_data)
    def test_fail_password(self, testdata):
        login = Login(self.driver)
        login.login(testdata["username"],testdata["password"])
        time.sleep(3)
        real = login.get_title()
        hope = testdata["hope"]
        self.assertEqual(real, hope)

    @data(*Test_data.fail_username_data)
    def test_fail_username_data(self, testdata):
        login = Login(self.driver)
        login.login(testdata["username"],testdata["password"])
        time.sleep(3)
        real = login.get_title()
        hope = testdata["hope"]
        self.assertEqual(real, hope)

    @data(*Test_data.fail_bost_data)
    def test_fail_bost(self, testdata):
        login = Login(self.driver)
        login.login(testdata["username"],testdata["password"])
        time.sleep(3)
        real = login.get_title()
        hope = testdata["hope"]
        self.assertEqual(real, hope)