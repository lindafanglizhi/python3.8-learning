import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

 #指定运行主机与端口号,也就是上一步在浏览器中输入的地址，只是换了之后的相对路径/grid/console换为/wd/hub

driver = webdriver.Remote(
     command_executor='http://localhost:5001/wd/hub',
     desired_capabilities=DesiredCapabilities.CHROME)

base_url='http://www.baidu.com/s'
driver.get(base_url)
driver.implicitly_wait(300)
driver.find_element_by_id('kw').send_keys("docker")
# driver.find_element_by_id("su").click()
print(driver.title)
time.sleep(1)
driver.close()