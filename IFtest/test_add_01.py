import unittest
from add import add_01


class TestAdd(unittest.TestCase):

    def setUp(self):
        print('在每个方法前执行，准备数据')
        self.a=''
        self.b=2
        self.sum=2.1

    def tearDown(self):
        print('在每个方法后执行，销毁数据')

    def test_add_01(self):
        result = add_01(self.a, self.b)
        assert self.sum == result
        print("测试相加")



if __name__ == '__main__':
    unittest.main()
