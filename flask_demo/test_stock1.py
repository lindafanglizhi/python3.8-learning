import requests
import pytest


@pytest.mark.parametrize(("size", "order"), [(10, "desc"), (20, "asc")])
def test_stock(size, order):
    '''
    https://xueqiu.com/service/v5/stock/screener/quote/list
    :param size:
    :return:
    ?page=1&size=30&order=desc&orderby=percent
    &order_by=percent&market=HK&type=hk&_=1553416305026
    '''
    url = 'https://xueqiu.com/service/v5/stock/screener/quote/list'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        # ,
        # 'xq_r_token': '843932e531acb61163845ae7ce15e4f2d4024790'

    }
    payload = {
        'page': 1, 'order_by': 'percent', 'order': str(order), 'size': str(size), 'market': 'HK','type': 'HK'
    }

    res = requests.get(url=url, headers=header, params=payload)

    result = res.json()
    print(result)
