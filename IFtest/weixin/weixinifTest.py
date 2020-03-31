import requests

# url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxad415a5cb4d2eb33&secret=dd1e098f51f0659cb29b50bd23939802'
# req = requests.get(url=url)
# print(req.status_code)
# print(req.json())
url = 'https://api.weixin.qq.com/cgi-bin/tags/create?access_token=29_LiYpykD7sZUrOtBq9aKgvRSzMIck-Z1LTjowzbIi7lVg2nfSW_vjb_8WJjmKFfucjQ3ArKPKjd6geh0XJ3Xry17Iu-APG4lP3GjI8xrF8I7UWd4ngArW9vV3kRUfm-8IbNfCHdy1NJLXfeU2JNZjAEAFJV'
data = {"tag": {"name": "世界和平2"}}
print(type(data))
req = requests.post(url=url, json=data)
req.encoding='utf8'
print(req.json())
