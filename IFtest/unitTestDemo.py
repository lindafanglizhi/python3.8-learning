import unittest


class unitDemoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('在整个类执行前执行一次，比如连接数据库')

    @classmethod
    def tearDownClass(cls):
        print('在整个类执行后执行一次，关闭数据库连接')

    def setUp(self):
        print('在每个测试方法前执行，一般初始化数据')

    def tearDown(self):
        print('在每个测试方法后执行，一般销毁数据')

    def test_get_01(self):
        print('这是测试方法1，全名要求包含_test或test_')

    # def test_post_02(self):
    #     print('测试方法2')


if __name__ == '__main__':
    unittest.main()