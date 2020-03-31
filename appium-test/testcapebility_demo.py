#coding=utf-8
from appium import webdriver
capabilities = {
    "platformName":"Android",
    "deviceName" : "192.168.56.101:5555",
   # "platformVersion": "7.0",
    "noReset":"true",
    "skipUnlock":"true",
    #"MobileCapabilityType.AUTOMATION_NAME":"uiautomator2",
    "app":"/Users/liz/Downloads/jinritoutiao_696.apk",
   # "broswerName":"Chrome"
    "appPackage":"com.ss.android.article.news",
    "appWaitActivity":"com.ss.android.article.news.activity.SplashBadgeActivity"

}
webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)