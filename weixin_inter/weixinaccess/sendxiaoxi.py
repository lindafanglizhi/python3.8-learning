
import requests
import pytest


def get_access_token():
    url ='https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwc88dd8afc4dcbc4b&corpsecret=6e8AFtQFI1UqSfF-O2_4EE16FM_8fn3DRrFOBwzU3xs'
    res_access = requests.post(url=url).json()['access_token']
    print(res_access)
    return res_access
get_access_token()


# def test_send_txt():
#     url1='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+get_access_token()
#
#     data ={
#            "touser" : "FangLiZhi",
#            # "toparty" : "PartyID1|PartyID2",
#            # "totag" : "TagID1 | TagID2",
#             "msgtype": "text",
#            "agentid" : 1000002,
#             "text": {
#                  "content" : "接口定义"
#             },
#            "safe":0
#         }
#
#     result=requests.post(url=url1,json=data)
#
#     print(result.json())
#         # assert result.json()['invaliduser']==""


