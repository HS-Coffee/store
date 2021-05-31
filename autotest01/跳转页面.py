from selenium import webdriver
import time
ff = webdriver.Chrome()
ff.get(r"G:\PycharmProjects\自动化day01\跳转页面\pop.html")
ff.maximize_window()
ff.find_element_by_xpath("//*[@id='goo']").click()
time.sleep(5)
ff.quit()