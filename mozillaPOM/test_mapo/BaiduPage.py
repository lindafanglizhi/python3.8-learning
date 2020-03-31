from pypom import Page
from selenium.webdriver.common.by import By


class Baidu(Page):
    _logo_locator = (By.CSS_SELECTOR, '#lg > map > area')
    _search_text = (By.ID, 'kw')
    _click_submit = (By.ID, 'su')

    def input_search(self, s_txt):
        self.find_element(*self._search_text).send_keys(s_txt)

    def click_submit(self):
        self.find_element(*self._click_submit).click()

    @property
    def loaded(self):
        logo = self.find_element(*self._logo_locator)
        return logo.is_enabled()

