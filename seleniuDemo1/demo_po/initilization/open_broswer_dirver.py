from selenium import webdriver


def build_up_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-infobars')
    driver = webdriver.Chrome(options=chrome_options,executable_path='/Users/lindafang/PycharmProjects/seleniuDemo1/chromedriver')
    driver.implicitly_wait(10)
    driver.get("https://www.douban.com/")
    return driver
