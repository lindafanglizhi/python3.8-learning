from seleniumDemo.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    input_box = (By.ID, 'kw')
    search_submit_btn = (By.XPATH, '//*[@id="su"]')
    news_link = (By.XPATH, '//*[@id="u1"]/a[@name="tj_trnews"]')

    def type_search(self, text):
        self.type(*self.input_box, text)

    def send_submit_btn(self):
        self.click(*self.search_submit_btn)

    def click_news(self):
        self.click(*self.news_link)
        self.sleep(2)
