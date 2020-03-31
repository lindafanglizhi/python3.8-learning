import requests

url = 'https://www.baidu.com/search?wd=selenium'
# 参数
headers={
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Cookie':'BAIDUID=CF6BE06289FFBA93070A81DA5DB45FC9:FG=1; BIDUPSID=CF6BE06289FFBA93070A81DA5DB45FC9; PSTM=1551425835; BD_UPN=123253; BDUSS=FlWdUtObVJTVVJwbGx2YlF0aHFrcFZYN0ZUY0V6Ny1uRWlISHlMM0MxQ2xSNXhjQVFBQUFBJCQAAAAAAAAAAAEAAABx4cc3a2lraW1pbWljaWNpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKW6dFylunRcT; MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; sug=3; sugstore=0; ORIGIN=2; bdime=0; H_PS_PSSID=1469_21115_30211_20691_22159; H_PS_645EC=e053v44AjuqVOFcgUyNIC3UXV5VuvBCVLg8ovWU%2Fk791lynI2j%2BSAuX6yX5xs5lyqzBL; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=1; BDSVRTM=126; COOKIE_SESSION=1388_0_9_9_19_2_0_0_9_2_0_0_0_0_0_0_1578637424_0_1578878653%7C9%23929247_67_1578011509%7C9'
}
# 发get请求
req = requests.get(url=url,headers=headers)
print(req.text)
# 加断言,判断python是否在返回的文本中
assert 'selenium' in req.text