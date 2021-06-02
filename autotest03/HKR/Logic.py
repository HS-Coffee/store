from selenium import webdriver

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def login(self,username,password):

        self.driver.find_element_by_id("loginname").send_keys(username)

        self.driver.find_element_by_id("password").send_keys(password)

        self.driver.find_element_by_id("submit").click()


    def get_title(self):
        return self.driver.title

    def get_error_info(self):
        return self.driver.find_element_by_id("msg_uname").text