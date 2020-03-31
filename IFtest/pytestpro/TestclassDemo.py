import pytest


# 导入pip 注意想着包的版本，pytest是高版本，pytest-remotedata低
# 文件名，测试用例搜索规则要求，test
# 测试类名  命名包含Test
# 测试方法的以test_开头
# 文件夹的名字或其他任何名字不能是关键字
def setup_module():
    print('不在类里面的在整个文件最前面执行')


def teardown_module():
    print('不在类里面的在整个文件最后执行')


def setup_function():
    print('不在类里面的在测试方法前执行')


def teardown_function():
    print('不在类里面的在测试方法后执行')

@pytest.mark.webtest
def test_one():
    pass
    print('不在类的测试方法1')


@pytest.mark.webtest
def test_two():
    print('不在类的测试方法2')
    assert 1==1


class TestClass(object):

    def setup_class(self):
        print('在整个类的前面执行')

    def teardown_class(self):
        print('在整个类的后面执行')

    def setup_method(self):
        print('在类里面的方法，在测试方法前执行')

    def teardown_method(self):
        print('在类里面的方法，在测试方法后执行')

    @pytest.mark.apptest
    def test_one(self):
        print('在类中的测试方法1')
        assert 'hello' in 'hello world'

    @pytest.mark.apptest
    def test_in_two(self):
        print('在类中的测试方法2')
        data={'name': 'linda', 'age': 18}
        data1={'name': 'linda', 'age': 18}
        # assert '18' in data
        assert data1 == data


