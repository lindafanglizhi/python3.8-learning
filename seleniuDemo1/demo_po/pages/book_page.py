from .basepage import BasePageObject
from selenium.webdriver.common.by import By


class BookPageObject(BasePageObject):
    _enter_read_book = (By.PARTIAL_LINK_TEXT, '豆瓣读书')
    _read_book_logo = (By.CLASS_NAME, 'nav-logo')
    _search_text = (By.ID, 'inp-query')
    _search_button = (By.CLASS_NAME, 'inp-btn')
    _book_name = (By.CLASS_NAME, 'title-text')

    def __init__(self):
        BasePageObject.__init__(self)

    def _locate_enter_read_book(self):
        return self.extend_find_element(BookPageObject._enter_read_book)

    def click_enter_read_book(self):
        self.click_element(self._locate_enter_read_book())

    def _locate_read_book_logo(self):
        return self.extend_find_element(BookPageObject._read_book_logo)

    def get_read_book_logo_text(self):
        self.get_element_text(self._locate_read_book_logo)

    def _locate_search_text(self):
        return self.extend_find_element(BookPageObject._search_text)

    def input_search_text(self, search_text):
        self.set_value(self._locate_search_text(search_text))

    def _locate_search_button(self):
        return self.extend_find_element(BookPageObject._search_button)

    def click_search_button(self):
        self.click_element(self._locate_search_button())

    def _locate_book_name(self):
        return self.extend_find_element(BookPageObject._book_name)

    def get_book_name_text(self):
        self.get_element_text(self._locate_book_name())

    def enter_soso_text(self,search_text):
        BookPageObject.click_enter_read_book()
        BookPageObject.input_search_text(search_text)
        BookPageObject.click_search_button()


