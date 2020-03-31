import requests

url = 'https://xueqiu.com/service/v5/stock/screener/quote/list?type=sha&order_by=percent&order=desc&size=10&page=1'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    # ,
    # 'xq_r_token': '843932e531acb61163845ae7ce15e4f2d4024790'

}
proxies = {
    'https': 'https://127.0.0.1:8888',
    'http': 'http://127.0.0.1:8888'
}
res = requests.get(url=url, headers=header, proxies=proxies, verify=False)
print(res.json())
