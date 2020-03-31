from appium import webdriver
from util import desired_cap
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,datetime

desired_caps = desired_cap.get_desired_capabilities("ApiDemos-debug.apk")
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

driver.find_element_by_accessibility_id("Accessibility").click()

# 加一个智能等待
WebDriverWait(driver,10).until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,"Accessibility Node Provider")))

# 通过mobileby的定位
driver.find_element(MobileBy.ACCESSIBILITY_ID,"Accessibility Node Provider").click()

# 返回键
driver.keyevent(4)
time.sleep(2)
# android自带的uiautomator自动化框架写的定位
driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Accessibility Node Querying")').click()

# 向上滑动（起始点的x/y是600，1500，终点x,y是600，1200)，，
# 如果终点的y大于 起始点是向下滑动，，如果向左向右，改变x的数值。
driver.swipe(600,1500,600,1200,500)

# 返回多个元素（checkbox），定位一个元素，可以分二步，先返回多人，用列表保存，取出索引中的第几个就行了。
# 查看是第几个，使用索引
driver.find_elements_by_class_name("android.widget.CheckBox")[2].click()

time.sleep(2)
driver.press_keycode(4)
# 智能等待
WebDriverWait(driver,10).until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,"Accessibility Service")))
# 截图，某一元素的图
driver.find_element_by_accessibility_id("Accessibility Service").screenshot("test.png")

time.sleep(2)
driver.press_keycode(4)
now=datetime.datetime.now().strftime('%Y-%m-%d')
# 整体截图
driver.save_screenshot(now+'.png')


