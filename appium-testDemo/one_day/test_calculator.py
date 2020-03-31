from appium import webdriver
import unittest

class TestCal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {
            "platformName": "android",
            "deviceName": "192.168.56.103:5555",
            "platformVersion": "7.0",
            "appPackage": "com.android.calculator2",
            "appActivity": "com.android.calculator2.Calculator",
        }

        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_calcu(self):
        self.driver.find_element_by_id("digit_7").click()
        self.driver.find_element_by_id("op_add").click()
        self.driver.find_element_by_id("digit_8").click()
        self.driver.find_element_by_id("eq").click()
        assert '15' == self.driver.find_element_by_id("result").text


if __name__ == '__main__':
    unittest.main()

