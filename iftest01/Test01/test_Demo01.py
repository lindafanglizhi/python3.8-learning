from ddt import ddt, data, unpack
import unittest

'''
在测试类上使用@ddt装饰符
测试方法上使用@data@unpack装饰符
@data装饰符把参数当作测试数据，参数可以是单个值、列表、元组、字典
'''


@ddt
class TestDdt(unittest.TestCase):

    @unittest.skip
    @data('你好', '你', '我')
    def test_Interface_01(self, value):  # value是参数，用于传递数据
        print(value)
        self.assertEqual('你', value)

    @unittest.skip
    @data([2], [3], [4])
    @unpack  # 解包，把列表的数据取出来
    def test_Interface_02(self, value):  # value是参数，用于传递数据
        print(value)
        self.assertEqual(3, value)

    @unittest.skip
    @data((1, 2), (2, 3))   # 同时传组数据
    @unpack  # 解包，把列表的数据取出来
    def test_Interface_03(self, value1, value2):  # value是参数，用于传递数据
        print(value1, value2)
        self.assertEqual(value1+1, value2)

    @data(({'num': 2}, {'name': 'linda'}), ({'num': 3}, {'name': 'tom'}))   # 同时传组数据
    # @unpack  # 解包，把列表的数据取出来
    def test_Interface_04(self, value1):  # value是参数，用于传递数据
        print(value1)
        # self.assertEqual(value1+1, value2)


if __name__ == '__main__':
    unittest.main()
