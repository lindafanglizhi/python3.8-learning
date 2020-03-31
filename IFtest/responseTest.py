import requests

req = requests.get('https://reqres.in/api/users?page=1')
# 返回二进制内容
# print(req.content)
# 返回发送的请求
# print(req.request)
# 返回响应以json格式
# print(req.json())
# 返回响应以文本格式
# print(req.text)
# 返回请求的url
# print(req.url)
# 返回头信息的某个属性值
# print(req.headers['Content-Type'])
# 返回编码
print(req.encoding)
# 返回发请求和回响应的总的时间
print(req.elapsed.total_seconds())
# 返回cookies的所有
# print(req.cookies)
# 如果有异常返回非none
print(req.raise_for_status())
