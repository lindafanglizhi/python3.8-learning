
from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestDoBanLogin(object):
    driver = None

    @pytest.fixture(scope="class")
    def open_browser(self):
        option = webdriver.ChromeOptions()
        option.add_argument('--disable-infobars')
        self.driver = webdriver.Chrome(options='chrome_options',executable_path='/Users/lindafang/PycharmProjects/seleniuDemo1/chromedriver')
        self.driver.get("https://www.douban.com/")
        self.driver.implicitly_wait(30)
        return self.driver

    @pytest.mark.parametrize('username,password',
                            [('18310107883', 'dbmyid88.'),
                             ('13888888888','12345678')
                            ])
    def test_dou_ban_login(self,open_browser, username, password):
        # 登陆页是一个frame的窗口,可以通过tag_name(标签名)返回第一个。
        self.driver = open_browser
        login_frame = self.driver.find_element_by_tag_name('iframe')

        # 切换到这个frame
        self.driver.switch_to.frame(login_frame)
        self.driver.implicitly_wait(10)

        # self.driver.execute_script("arguments[0].style.background = 'rgb(138,43,226 )';", login_frame)
        # 使用classname中有空格，是空格两边的name都可用。你搜索定位一下是否唯一，不唯一可以用列表[0]
        self.driver.find_element_by_class_name('account-tab-account').click()
        ele = self.driver.find_element_by_id('username')
        # WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(ele))
        ele.send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_link_text('登录豆瓣').click()
        self.driver.implicitly_wait(10)
        assert "我的豆瓣" == self.driver.find_element_by_partial_link_text('我的豆瓣').text

    @pytest.fixture(scope="class")
    def tearDown(self):
        print("end")
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(["-s", "test_login_pytest.py"])


