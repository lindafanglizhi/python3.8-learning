import requests,unittest
from parameterized import parameterized


class TestCaseSearch(unittest.TestCase):
    def setUp(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36\
         (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Cookie': 'xq_a_token=8309c28a83ae5d20f26b7fcc22debbcd459794bd'

        }

    @parameterized.expand([
        ('pinyin', 'pdd'),
        ('hanzi', '拼多多'),
        ('4gezi', '中国平安'),
        ('teshufuhao', '中@#$%^')
    ])
    def test_search(self,_,data):
        url = 'https://xueqiu.com/stock/search.json?code='+data+'&size=3&page=1'
        print(url)
        res = requests.get(url=url,  headers=self.headers)
        result = res.json()
        assert 200 == res.status_code
        assert data in result['stocks'][0]['name']
        print(res.elapsed.total_seconds())
        assert 1 >= res.elapsed.total_seconds()


