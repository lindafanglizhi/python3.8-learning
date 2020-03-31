
from appium import webdriver

desired_caps = {
        'platformName': 'Android',
        'deviceName': '192.168.56.103:5555',
        'platformVersion': '7.0',
        'appPackage': 'com.android.calculator2',
        'appActivity': 'com.android.calculator2.Calculator'
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


driver.find_element_by_id("digit_7").click()
driver.find_element_by_accessibility_id("plus").click()
driver.find_element_by_id("digit_8").click()
driver.find_element_by_accessibility_id("equals").click()
