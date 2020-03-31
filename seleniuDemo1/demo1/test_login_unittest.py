
from selenium import webdriver
import unittest


class TestDouBanLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/Users/lindafang/PycharmProjects/seleniuDemo1/chromedriver')

        self.driver.get("https://www.douban.com/")

    def test_dou_ban_login(self):

        # 登陆页是一个frame的窗口,可以通过tag_name(标签名)返回第一个。
        login_frame = self.driver.find_element_by_tag_name('iframe')
        #  不想带控制条
        option = webdriver.ChromeOptions()
        option.add_argument('--disable-infobars')
        # 切换到这个frame
        self.driver.switch_to.frame(login_frame)

        # 使用classname中有空格，是空格两边的name都可用。你搜索定位一下是否唯一，不唯一可以用列表[0]
        self.driver.find_element_by_class_name('account-tab-account').click()
        self.driver.find_element_by_id('username').send_keys('18310107883')
        self.driver.find_element_by_id('password').send_keys('dbmyid88.')
        self.driver.find_element_by_link_text('登录豆瓣').click()
        self.driver.implicitly_wait(10)
        assert "我的豆瓣" == self.driver.find_element_by_partial_link_text('我的豆瓣').text


    def tearDown(self):
        print("end")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


