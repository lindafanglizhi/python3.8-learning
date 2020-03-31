import requests
import pytest
from .util_read_yaml import read_yaml


# test_data=[{"tag": {"name": "linda73"}},{"tag": {"name": "linda74"}}]
# print(type(test_data))

@pytest.fixture()
def get_base_data(self):
    base_data = read_yaml("test_http_data.yaml")
    return base_data.values()


@pytest.fixture()
def get_test_data():
    test_data = read_yaml("test_data.yaml")
    print(type(test_data['payload']))
    return test_data


@pytest.fixture()
def query_param(request):
    print(request.param)
    return request.param


    # 3、在测试方法中....
@pytest.mark.parametrize('query_param',get_test_data)
def test_add_tag(get_access_token,get_base_data,query_param):
        # adata =testdata['tag']['name']
    print(query_param)
        # url=get_base_data['url'] + get_access_token
        # method =get_base_data.get('method')
        # print(url,method)
        # req = requests.request(method=method, url=url, json=testdata)
        # print(req.json())
        # assert adata == req.json()['tag']['name']

