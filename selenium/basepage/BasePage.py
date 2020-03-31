'''
   Page Object模式是Selenium中的一种测试设计模式，主要是将每一个页面设计为一个Class，其中包含页面中需要测试的元素（按钮，输入框，标题 等），
这样在Selenium测试页面中可以通过调用页面类来获取页面元素，
这样巧妙的避免了当页面元素id或者位置变化时，需要改测试页面代码的情况。 当页面元素id变化时，只需要更改测试页Class中页面的属性即可。
    Page Object模式是一种自动化测试设计模式，将页面定位和业务操作分开，分离测试对象（元素对象）和测试脚本（用例脚本），提高用例的可维护性。
    unittest是一种单元测试框架，用于设计各式各样的测试用例，可调用PageObject设计的页面类（对象），设计出更加可维护的用例。
它提供用例组织与执行，提供丰富的比较（断言）方法，提供丰富的日志，统一适用于web自动化用例的开发与执行。

'''
'''
1.定义页面基础类，封装所有页面公用的方法。
Project:基础类BasePage，封装所有页面都公用的方法，
定义open函数，重定义find_element，switch_frame，send_keys等函数。
在初始化方法中定义驱动driver，基本url，title
WebDriverWait提供了显式等待方式。

'''

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """
    BasePage封装所有页面都公用的方法，例如driver, url ,FindElement等
    """

    # 初始化driver、url、page_title等
    # 实例化BasePage类时，最先执行的就是__init__方法，该方法的入参，其实就是BasePage类的入参。
    # __init__方法不能有返回值，只能返回None
    # self只实例本身，相较于类Page而言。
    def __init__(self, selenium_driver, base_url, page_title):
        self.driver = selenium_driver
        self.base_url = base_url
        self.page_title = page_title

    # 通过title断言进入的页面是否正确。
    # 使用title获取当前窗口title，检查输入的title是否在当前title中，返回比较结果（True 或 False）
    def on_page(self, page_title):
        return page_title in self.driver.title

    # 打开页面，并校验页面链接是否加载正确
    # 以单下划线_开头的方法，在使用import *时，该方法不会被导入，保证该方法为类私有的。
    def _open(self, url, page_title):
        # 使用get打开访问链接地址
        self.driver.get(url)
        self.driver.maximize_window()
        # 使用assert进行校验，打开的窗口title是否与配置的title一致。调用on_page()方法

        assert self.on_page(page_title), "打开开页面失败 %s" % url

    # 重写元素定位方法
    def find_element(self, *loc):
        # return self.driver.find_element(*loc)
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            # WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except AttributeError:
            print("%s 页面中未能找到 %s 元素" % (self, loc))

    # 重写switch_frame方法
    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    # 定义script方法，用于执行js脚本，范围执行结果
    def script(self, src):
        self.driver.execute_script(src)

    # 重写定义send_keys方法
    def send_keys(self, loc, vaule1, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule1)
        except AttributeError:
            print("%s 页面中未能找到 %s 元素" % (self, loc))

