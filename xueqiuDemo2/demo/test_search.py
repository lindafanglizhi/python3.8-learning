# pip install requests
import requests
from bs4 import BeautifulSoup
import lxml

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36\
 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Cookie': 'xq_a_token=8309c28a83ae5d20f26b7fcc22debbcd459794bd'

}
'''
https://xueqiu.com/stock/search.json?code=中国平安&size=3&page=1
'''
param = {'code':'中国平安','size':3,'page':1
}

url = 'https://xueqiu.com/stock/search.json'
res = requests.get(url=url, params=param,headers=headers)
result = res.json()
assert 200 == res.status_code
assert '中国平安' in result['stocks'][0]['name']
print(res.elapsed.total_seconds())
assert 1 >= res.elapsed.total_seconds()

