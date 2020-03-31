import requests


def get_access_token():
    url ='https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwc88dd8afc4dcbc4b&corpsecret=6e8AFtQFI1UqSfF-O2_4EE16FM_8fn3DRrFOBwzU3xs'
    res_access = requests.post(url=url).json()['access_token']
    print(res_access)
    return res_access

