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
https://xueqiu.com/stock/search.json?code=%E4%B8%AD%E5%9B%BD%E5%B9%B3%E5%AE%89&size=3&page=1
'''

res = requests.get('https://xueqiu.com/', headers=headers).text
# print(res.text)

html = BeautifulSoup(res, 'lxml')
print(html.title.get_text())
assert "雪球" in html.title.get_text()
