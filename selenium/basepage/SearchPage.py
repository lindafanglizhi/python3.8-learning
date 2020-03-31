'''

Project:页面基本操作方法：如open，input_username，input_password，click_submit
'''
from selenium.webdriver.common.by import By
from basepage.BasePage import BasePage


# 继承BasePage类
class SearchPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    search_text_loc = (By.ID, 'kw')
    s_baidu_buton_loc = (By.ID, 'su')

    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.page_title)

    # 输入用户名：调用send_keys对象，输入用户名
    def input_search(self, search_text):
        self.find_element(*self.search_text_loc).send_keys(search_text)

    # 点击登录：调用send_keys对象，点击登录
    def click_submit(self):
        self.find_element(*self.s_baidu_buton_loc).click()


