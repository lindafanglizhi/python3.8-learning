import os


def PATH(apk):
    # 返回当前路径与Apk组合在一起的绝对路径
    return os.path.abspath(os.path.join(os.path.dirname(__file__),apk))


def get_desired_capabilities(app=None):
    desired_caps = {
        "platformName": "android",
        "deviceName": "192.168.56.103:5555",
        "platformVersion": "7.0",
        "automationName":"UIAutomator2",
        # "newCommandTimeout":240,
        "unicodeKeyboard": True,
        "resetKeyboard": True,
    }
    if app is not None:
        # 返回上一级(..)的下面的apps路径 下的APP的绝对地址（上上级../..）
        desired_caps['app']=PATH(os.path.join('..','apps',app))
    return desired_caps