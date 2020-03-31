from appium import webdriver


# 连接一下模拟器的设备:y
# 设备名：192.168.56.103:5555

desired_caps = {
  "platformName": "android",
  "deviceName": "192.168.56.103:5555", # adb devices
  "platformVersion": "7.0",#android 版本
  "appPackage": "com.android.calculator2",  #包名，开发代码工程的路径 logcat，dumpsys
  "appActivity": "com.android.calculator2.Calculator",  #代码中主程序
  # "unicodeKeyboard": True,
  # "resetKeyboard": True,
  # "autoGrantPermissions": True
}

# desired_caps1 = {
#   "platformName": "android",
#   "deviceName": "192.168.56.103:5555",
#   "app":"/Users/lindafang/PycharmProjects/appium-testDemo/one_day/ApiDemos-debug.apk"
# }

driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

driver.find_element_by_id("digit_7").click()
driver.find_element_by_id("op_add").click()
driver.find_element_by_id("digit_8").click()
driver.find_element_by_id("eq").click()
# 断言
# 自动化测试框架跑：unittest/pytest、PageObject、DDT




