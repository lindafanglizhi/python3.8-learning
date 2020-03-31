import requests



'''
DxF5qeh-wz6gHyd2bkSJi0ozszjMs5yYgoSIRdx7ueGFUqjRfTscSF4dtXhD-UOIsJ82y5p3psQSOFTOEgOsyyLWMVQUTgsL7tVvYdKn1f3mw94FeCfKlnllHItW0c8yyRkFmYWTxLG2xPhh-Zehz6ZV_9UFNbdxZiNbj7eTQ-NsEJ8uZCMDpQJCrOWGpti9ARNP0nP496ggWFglFc16kQ
POST https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token=accesstoken001&type=file HTTP/1.1
Content-Type: multipart/form-data; boundary=-------------------------acebdf13572468
Content-Length: 220
---------------------------acebdf13572468
Content-Disposition: form-data; name="media";filename="wework.txt"; filelength=6
Content-Type: application/octet-stream
mytext
---------------------------acebdf13572468--


'''
access_token='tC_AsjW0WYTQuXOPj69ezFjX4KLducq7NTUI2V0J8RPAPZLMpdNeLJLjAT-wYBoBAvkux238BLEdB1HfaxZ-PVs3VHCwHCHzc1KViGeImlS0pIiwRSvIrvMUrcVa3SwK-iBLm0Xy4b3qn_saHUG24AvZIILxlqOz1gxuVlZAn7EyaXVI3RfVTfx3MwqeLaeqIoB0C4zMzcGAuJhAhANY8w'
url ='https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token='+access_token+'&type=image'
headers ={
    'Content-Type':'multipart/form-data',
}
# files={'name':'2.png'}
files={'media':('fang.jpg',open('2.png','rb'),'image/jpg')}
result=requests.post(url=url, headers=headers,files=files)
media_id=result.json()['media_id']



url2='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+access_token
data ={
   "touser" : "FangLiZhi",
   # "toparty" : "PartyID1|PartyID2",
   # "totag" : "TagID1 | TagID2",
   "msgtype" : "image",
   "agentid" : 1000002,
   "image" : {
        "media_id" : media_id
   },
   "safe":0
}

'''
url2='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+access_token
data={
   "touser" : "F",
   "toparty" : "PartyID1|PartyID2",
   "totag" : "TagID1 | TagID2",
   "msgtype" : "image",
   "agentid" : 1,
   "image" : {
        "media_id" : "MEDIA_ID"
   },
   "safe":0
}
'''
rs=requests.post(url=url2,json=data)
print(rs.json())