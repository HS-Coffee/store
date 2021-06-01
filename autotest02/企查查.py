from selenium import  webdriver
from selenium.webdriver import ActionChains
import  time

driver = webdriver.Chrome()
driver.get("https://www.qcc.com")
driver.maximize_window()


time.sleep(6)
# 取消框
driver.find_element_by_xpath("//*[@id='addfavorModal']/div/div/div[1]").click()

driver.find_element_by_link_text("登录 | 注册").click()
time.sleep(5)
tag = driver.find_element_by_xpath("//*[@id='nc_1_n1z']")

ac = ActionChains(driver)
for i in range(0,35):
    ac.click_and_hold(tag).move_by_offset(i*10,0).perform()