from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome(executable_path='/Users/lindafang/PycharmProjects/seleniumDemo/drvier/chromedriver')
url = "https://www.baidu.com"
driver.get(url)
time.sleep(3)
mouse = driver.find_element(By.LINK_TEXT, "设置")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(3)
driver.find_element(By.LINK_TEXT, "搜索设置").click()
time.sleep(3)
s = driver.find_element(By.ID, "nr")
Select(s).select_by_visible_text("每页显示50条")


# driver.find_element("id", "gxszButton").click()
# driver.find_element("class name", "prefpanelgo").click()

js = 'document.getElementsByClassName("prefpanelgo")[0].click();'
driver.execute_script(js)