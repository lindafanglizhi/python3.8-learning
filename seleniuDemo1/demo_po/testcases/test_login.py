#! /usr/bin/env python
#coding=utf-8

import pytest

from pages.book_page import BookPageObject
from pages.loginpage import LoginPageObject

#
# @pytest.mark.parametrize('username, password',
#                          [('18310107883', 'dbmyid88.')
#                          ])
# def test_douban(username, password):
#
#     login_page_object = LoginPageObject()
#     '''
#     #allure.step
#     login_page_object.switch_to_login_frame()
#     #allure step
#     login_page_object.click_login_tab()
#     #allure step
#     login_page_object.input_user_name(username)
#     # allure step
#     login_page_object.input_password(password)
#
#     login_page_object.click_login_button()
#     '''
#     login_page_object.login(username,password)
#
#     text = login_page_object.get_my_douban_text()
#     assert text == "我的豆瓣"
#

@pytest.mark.parametrize('searchtext',
                         [('python')
                         ])
def test_book(searchtext):
    book_page = BookPageObject()
    print(searchtext)
    book_page.enter_soso_text(searchtext)
    # print(book_page.get_book_name_text())


if __name__ == '__main__':
    pytest.main(["-sq", "test_login.py"])

