from selenium import webdriver
from selenium.webdriver import ActionChains
import time

ff = webdriver.Firefox()
ff.get("http://taobao.com")
ff.maximize_window()
#鉴于推广位及数据变化太大,遂选择小众商品进行试验!
ff.find_element_by_xpath("//*[@id='q']").send_keys("俄罗斯军粮")
ff.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[1]/div[2]/form/div[1]/button").click()
#此处扫码登录
ff.find_element_by_xpath("//html/body/div/div[2]/div[3]/div/div/div/div[1]/i").click()
time.sleep(15)

#鉴于推广位及数据变化太大,遂选择小众商品进行试验!
ff.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/div[21]/div/div/div[1]/div[4]/div[1]/div/div[1]").click()

wins = ff.window_handles  # ["asdf105as1fa50ds1fa5df","1a05sd1fa651f6as5f1a65df"]
print(wins)
ff.switch_to.window(wins[1])

time.sleep(3)
ff.find_element_by_xpath("/html/body/div[5]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div/div[7]/div/div[3]/div[2]/a").click()

time.sleep(3)
ff.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[4]/a[2]").click()