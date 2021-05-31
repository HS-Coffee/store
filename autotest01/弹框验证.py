from selenium import webdriver
import time
ff=webdriver.Chrome()
ff.get(r"G:\PycharmProjects\自动化day01\弹框的验证\dialogs.html")
ff.maximize_window()
ff.find_element_by_xpath("//*[@id='alert']").click()
ff.switch_to.alert.accept()
ff.find_element_by_xpath("//*[@id='confirm']").click()
ff.switch_to.alert.dismiss()
ff.quit()