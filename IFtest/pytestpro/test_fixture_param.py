import pytest


# # 登陆login,多次登陆（login在支付之前，数据驱动）
# 数据的形式多种{'name':'linda','password':'88888'}
# {'name':'tom','password':'88888'}

@pytest.fixture(params=['linda',2])
def login(request):
    print('登陆')
    return request.param
#
# # 测试支付pay，不同用户支付
def test_pay(login):
    print('username:%s' % login)
    print('支付')
#

# @pytest.fixture(params=[1, 2, 3])
# def test_data(request):
#     return request.param
#
#
# def test_one(test_data):
#     print('\ntest data: %s' % test_data)

