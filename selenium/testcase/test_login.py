import unittest
from basepage.SearchPage import SearchPage
from selenium import webdriver


class TestBaiduSou(unittest.TestCase):
    """
baidu search
    """

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/lindafang/PycharmProjects/selenium/testcase/chromedriver')
        self.driver.implicitly_wait(30)
        self.url = "http://www.baidu.com"
        self.search_text = "pageobject"


    # 用例执行体
    def test_ss(self):
        # 声明LoginPage类对象
        search_page = SearchPage(self.driver, self.url, "百度")
        # 调用打开页面组件
        search_page.open()
        # 搜索
        search_page.input_search(self.search_text)
        # 提交
        search_page.click_submit()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

