from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='/Users/lindafang/PycharmProjects/seleniumDemo/drvier/chromedriver')
driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("allure")
t1 = driver.find_element(By.LINK_TEXT, "视频").text
print(t1)
t2 = driver.find_element(By.NAME, "tj_trhao123").text
time.sleep(2)
print(t2)
t3 = driver.find_element(By.CLASS_NAME, "bri").text
time.sleep(2)
print(t3)
driver.find_element(By.ID, "kw").send_keys("pytest")
driver.find_element_by_id("kw").send_keys("allure")
driver.find_element(By.CSS_SELECTOR, "#su").click()

driver.quit()
