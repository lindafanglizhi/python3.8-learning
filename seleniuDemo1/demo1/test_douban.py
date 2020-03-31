import time

from selenium import webdriver
import unittest

class Test_douban(unittest.TestCase):

    def test_douban(self):
        driver = webdriver.Chrome(executable_path='/Users/lindafang/PycharmProjects/seleniuDemo1/chromedriver')

        driver.get("https://www.douban.com/")
        # 登陆页是一个frame的窗口,可以通过tag_name(标签名)返回第一个。
        login_frame = driver.find_element_by_tag_name('iframe')
        # 切换到这个frame
        driver.switch_to.frame(login_frame)
        # 通过class_name找到验证码
        forget = driver.find_element_by_class_name('account-form-link')
        forget.click()
        time.sleep(2)
        # 跳转后是新的窗口
        open_windows = driver.window_handles
        driver.switch_to.window(open_windows[1])
        print(str(open_windows))
        print(driver.title)
        assert "帐号 使用帮助" == driver.title
        print("end")
        driver.quit()


if __name__ == '__main__':
    unittest.main()


