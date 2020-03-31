'''
https://accounts.douban.com/j/mobile/login/basic
'ck':'','name':'18310107883','password':'dbmyid88.','remember':'false','ticket':''
'''

import requests
import pytest


def test_stock():

    url = 'https://accounts.douban.com/j/mobile/login/basic'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        # ,
        # # 'Content-Type': 'application/x-www-form-urlencoded'
        # 'Content-Type': 'application/json; charset=utf-8'
        # 'xq_r_token': '843932e531acb61163845ae7ce15e4f2d4024790'

    }
    payload = {
        'ck': '', 'name': '18310107883', 'password': 'dbmyid88.', 'remember': 'false', 'ticket':''
    }

    res = requests.post(url=url, headers=header, json=payload, verify=False)

    result = res.json()
    print(result)
