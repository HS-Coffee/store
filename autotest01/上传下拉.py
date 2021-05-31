from selenium import webdriver
import time
ff = webdriver.Chrome()
ff.get(r"G:\PycharmProjects\自动化day01\上传文件和下拉列表\autotest.html")
ff.maximize_window()
ff.find_element_by_xpath("//*[@id='accountID']").send_keys("coffee")
ff.find_element_by_xpath("//*[@id='passwordID']").send_keys("coffee")
ff.find_element_by_xpath("//*[@id='areaID']").send_keys("青岛市")
ff.find_element_by_xpath("//*[@id='sexID2' and @name='u2']").click()
ff.find_element_by_xpath("//*[@value='winter']").click()
ff.find_element_by_xpath("//*[@name='file']").send_keys(r"G:\图片\1\1.jpg")
ff.find_element_by_xpath("//*[@id='buttonID']").click()
ff.switch_to.alert.accept()
ff.quit()