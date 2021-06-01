from selenium import webdriver
from selenium.webdriver import ActionChains
import time
ff = webdriver.Chrome()
ff.get("https://www.bilibili.com")
ff.maximize_window()
time.sleep(1)
ff.find_element_by_xpath("//*[@class='unlogin-avatar']").click()
# show = ff.current_window_handle
# print(show)
time.sleep(3)

#获取句柄
win = ff.window_handles
print(win)
#切换窗口
ff.switch_to.window(win[1])

time.sleep(2)
ff.find_element_by_xpath("//*[@id='geetest-wrap']/div/div[1]/span[1]").click()
#扫码登陆


time.sleep(20)


tag = ff.find_element_by_xpath("//*[@id='internationalHeader']/div[1]/div/div[3]/div[2]/div[5]")
#action chain 事件链
#将整个页面交给他管理
ac = ActionChains(ff)
ac.move_to_element(tag).perform()
time.sleep(2)
ff.find_element_by_xpath("//*[@id='nav_searchform']/input").send_keys("匪 帮 哥 哥")
ff.find_element_by_xpath("//*[@id='nav_searchform']/div").click()

time.sleep(2)
win = ff.window_handles
tag = len(win)-1
ff.switch_to.window(win[tag])

ff.find_element_by_xpath("//*[@id='all-list']/div[1]/div[2]/ul/li[1]/a/div").click()

win = ff.window_handles
tag = len(win)-1
ff.switch_to.window(win[tag])

time.sleep(3)
ff.find_element_by_xpath("//*[@id='bilibiliPlayer']/div[1]/div[1]/div[11]/div[2]/div[2]/div[3]/div[10]/button[1]/span").click()


time.sleep(5)




