import requests

url = 'https://cn.bing.com/search?q=python'
# 参数

# 发get请求
req = requests.get(url=url)
# print(req.text)
# 加断言,判断python是否在返回的文本中
assert 'python' in req.text