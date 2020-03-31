from appium import webdriver
import time

desired_caps1 = {
    "platformName": "android",
    "deviceName": "192.168.56.103:5555",
    "platformVersion": "7.0",
    "app":"/Users/lindafang/PycharmProjects/appium-testDemo/one_day/"
        "youdaonote_android_6.7.18_youdaoweb.apk",
    "noReset":True
#     http://appium.io/docs/cn/writing-running-appium/caps/

}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps1)

driver.find_element_by_id("com.youdao.note:id/btn_ok").click()
time.sleep(1)
driver.find_element_by_id("com.youdao.note:id/btn_ok").click()
time.sleep(1)
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
time.sleep(5)
# driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
# time.sleep(2)
print(driver.page_source)
driver.tap([(576,2488),(864,2536)],500)
# [576,2564][864,2768]
driver.find_element_by_id("com.youdao.note:id/add_note").click()

time.sleep(2)
driver.find_element_by_id("com.youdao.note:id/add_icon").click()
time.sleep(2)
driver.find_element_by_id("com.youdao.note:id/note_title").send_keys("这是我要记得日记")
time.sleep(4)
# driver.find_element_by_accessibility_id("Android BulbEditor").\
#     send_keys("今天心情不错，打算吃100个饺子")

driver.find_element_by_class_name("android.widget.EditText").send_keys("今天心情不错，打算吃100个饺子")

time.sleep(4)
driver.find_element_by_id("com.youdao.note:id/actionbar_complete_text").click()
driver.reset()
driver.close_app()
driver.remove_app("com.youdao.note")


