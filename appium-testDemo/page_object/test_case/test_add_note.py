import unittest
from util import desired_cap
from appium import webdriver
from page_object.pages import AddNotePages
from ddt import ddt,data
from util.get_csvdata import get_csv_data

@ddt
class TestNote(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_cap_value = desired_cap.get_desired_capabilities("youdaonote_android_6.7.18_youdaoweb.apk")
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap_value)
        # 先初始化页面，
        ok = AddNotePages.FirstOpenPage(cls.driver)
        # 操作的方法
        ok.permission_allowandok()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # cls.driver.remove_app("com.youdao.note")

    @data(*get_csv_data("/Users/lindafang/PycharmProjects/appium-testDemo/datafile/add_note.csv"))
    def test_addNote(self,value):
        daily_title =value[0]
        daily_text =value[1]
        # 先初始化添加日记的页面
        addnote=AddNotePages.AddNotePage(self.driver)
        addnote.add_note_ok(daily_title,daily_text)


if __name__ == '__main__':
    unittest.main()
