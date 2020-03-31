from appium import webdriver
from util import desired_cap
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_cap_value =desired_cap.get_desired_capabilities("youdaonote_android_6.7.18_youdaoweb.apk")
driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cap_value)


driver.find_element_by_id("com.youdao.note:id/btn_ok").click()
time.sleep(1)
driver.find_element_by_id("com.youdao.note:id/btn_ok").click()
time.sleep(1)
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
time.sleep(5)
driver.find_elements_by_id("com.youdao.note:id/tab_name")[3].click()
time.sleep(2)

driver.swipe(660,1369,660,900,500)
print(driver.current_context)
driver.find_element_by_id("com.youdao.note:id/youdao_reading").click()
print(driver.contexts)
print(driver.current_context)
time.sleep(2)
driver.find_elements_by_accessibility_id("2011")[0].click()
print(driver.contexts)
print(driver.current_context)
driver.find_element_by_accessibility_id("选择话题").click()




# print(driver.current_context)
# el3 = driver.find_element_by_id("com.youdao.note:id/image_2")
# el3.click()
# print(driver.current_context)
# el4 = driver.find_elements_by_class_name("android.widget.ImageView")
# el4[2].click()
#
# print(driver.contexts)



#
#
#
# driver.tap([(576,2488),(864,2536)],500)
#
# driver.find_element_by_id("com.youdao.note:id/add_note").click()
# time.sleep(1)
# driver.find_element_by_id("com.youdao.note:id/add_note_floater_add_note").click()
# time.sleep(4)
# driver.find_element_by_id("com.youdao.note:id/note_title").send_keys("我的日记")
# time.sleep(4)
# # ele = driver.find_element_by_accessibility_id('Android BulbEditor').find_element_by_class_name('android.widget.EditText')
# # time.sleep(1)
# # ele.send_keys("这个为什么呢？")
# # driver.keyevent(40)
# # driver.keyevent(37)
# # driver.keyevent(42)
# # driver.keyevent(32)
# # driver.keyevent(29)
# # WebDriverWait(driver,10).until(EC.presence_of_element_located((MobileBy.CLASS_NAME,"android.widget.EditText")[1]))
# # driver.find_elements_by_class_name("android.widget.EditText")[1].send_keys("我郁闷")
# # driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='Android BulbEditor']/android.view.View").send_keys("定位空")
# # driver.find_elements_by_xpath("//*[@class=android.widget.EditText]")[1].send_keys("xpath")
#
# ele=driver.find_elements_by_class_name("android.widget.EditText")[1]
# time.sleep(3)
# ele.send_keys("我改了")
#
# driver.remove_app("com.youdao.note")