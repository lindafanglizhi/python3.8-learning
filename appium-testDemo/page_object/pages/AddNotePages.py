from .BasePageM import BasePage
from .locators import FirstOpenPageLocators
from .locators import AddNotePageLoacators


class FirstOpenPage(BasePage):
    # 继承的：BasePage是我的父类，父类中的所有方法我都能用。


    def permission_allowandok(self):
        BasePage.click_thing(self,FirstOpenPageLocators.btn_ok)
        BasePage.click_thing(self,FirstOpenPageLocators.btn_ok)
        BasePage.click_thing(self,FirstOpenPageLocators.permission_allow)


class AddNotePage(BasePage):
    def add_note_ok(self,title, editText):
        BasePage.click_thing(self,AddNotePageLoacators.add_note)
        BasePage.click_thing(self, AddNotePageLoacators.add_icon)
        BasePage.set_value(self, AddNotePageLoacators.note_title,title)
        BasePage.set_value(self,AddNotePageLoacators.note_editText,editText)
        BasePage.click_thing(self, AddNotePageLoacators.submit_complete)
        # BasePage.save_pic(self, "1.png")


