from selenium import webdriver
import time

class Login:

    def __init__(self,driver):
        self.driver = driver

    #登陆系统
    def login(self,username,password):
        self.driver.find_element_by_id("userName").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_id("btn_login").click()
        # time.sleep(5)
        # self.driver.find_element_by_xpath("//*[@id='root']/div[4]/div/div[1]").click()
        # self.driver.find_element_by_xpath("//*[@id='618report']/div").click()

    def get_title(self):
        return self.driver.title
# driver = webdriver.Chrome()
# driver.get("https://www.ningmengyun.com/")
# driver.maximize_window()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@class='menu-btn-login']").click()
# time.sleep(1)
# driver.find_element_by_xpath("//*[@class='toggle-container']").click()
# logic = Login(driver)
# # from Login_data import Test_data
# # data = Test_data.success_data()
# # username = data.success_data["username"]
# # password = data.success_data["password"]
# # print(username,"\t",password)
# logic.login("16653231839","123456")
