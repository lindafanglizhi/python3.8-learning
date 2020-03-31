import pytest

# 凡是数据或方法或有人共享的可以写在这
@pytest.fixture(scope='module')
def con_db():
    print("连接数据库")
    print("打开浏览器")
    yield
    print("关闭浏览器")
    print("断开连接数据库")

@pytest.fixture(params=[{'name':'linda','age':18},{'name':'qing','age':38}])
def login(request,open_browser):
    print("登陆名："+request.param['name'])


@pytest.fixture()
def open_browser():
    print('打开支付页！')
    yield
    print('关闭支付页！')