import pytest
import requests


@pytest.fixture(scope='module')
def get_access_token():
    url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxad415a5cb4d2eb33&secret=dd1e098f51f0659cb29b50bd23939802'
    req=requests.get(url=url)
    # print(req.json()['access_token'])
    return req.json()['access_token']

