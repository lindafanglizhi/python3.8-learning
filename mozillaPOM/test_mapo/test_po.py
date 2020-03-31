from selenium.webdriver import Chrome
from test_mapo.BaiduPage import Baidu
import time


driver = Chrome(executable_path=
                '/Users/lindafang/PycharmProjects/mozillaPOM/chromedriver')
base_url = 'http://www.baidu.com/'

page = Baidu(driver, base_url).open()

page.input_search("pageobject")
page.click_submit()
time.sleep(2)
print(driver.title)
assert "pageobject" in driver.title
driver.close()



