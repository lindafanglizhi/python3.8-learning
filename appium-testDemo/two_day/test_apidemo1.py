from appium import webdriver
from util.desired_capabilities import PATH,get_desired_capabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.select import Select
import time,os,datetime,base64

desired_caps = get_desired_capabilities('ApiDemos-debug.apk')
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 录制屏幕，只支持android8以上
driver.start_recording_screen()
# 以二进制数据形式获取当前窗口屏幕截图
driver.get_screenshot_as_png()
# 直接调用
driver.find_element_by_accessibility_id("Accessibility").click()
# 智能等待，元素出现
WebDriverWait(driver,10).until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,"Accessibility Node Querying")))
# 使用封装的MobileBy，将从selenium中的继承的By与手机中的合并统一为MobileBy（因为selenium中没有accessibilityid）
driver.find_element(MobileBy.ACCESSIBILITY_ID,"Accessibility Node Provider").click()

# 以文件形式获取当前窗口屏幕截图
driver.save_screenshot("test"+datetime.datetime.now().strftime('%Y-%m-%d')+".png")
# 使用手机的返回键
driver.keyevent(keycode=4)
# 使用android自带的自动化框架uiautomator定位
time.sleep(1)
driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Accessibility Node Querying")').click()
time.sleep(1)
driver.swipe(320,1526,320,1075,500)
time.sleep(1)
driver.find_elements_by_class_name("android.widget.CheckBox")[2].click()

time.sleep(1)
driver.press_keycode(4)
driver.keyevent(keycode=4)
driver.find_element(MobileBy.ACCESSIBILITY_ID, "Animation").screenshot("test.png")
driver.find_element_by_accessibility_id("Animation").click()
#
# el = driver.find_element_by_class_name('android.widget.ListView')
#
# el.find_elements_by_accessibility_id('Bouncing Balls').click()
payload = driver.stop_recording_screen()
video_path = os.path.join(os.getcwd(),datetime.datetime.now().strftime('%Y-%m-%d')+ '.mp4')
with open(video_path, "wb") as fd:
    fd.write(base64.b64decode(payload))


