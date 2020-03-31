import unittest
import requests
import time
import os
from HTMLTestRunner import HTMLTestRunner


class unitDemoTest(unittest.TestCase):

    def setUp(self):
        self.url='https://reqres.in/api/users?page=1'

    def tearDown(self):
        print('结束测试')

    def test_get_01(self):
        req = requests.get(url=self.url)
        req_json_data = req.json()['data']
        # unittest测试框架的断言，断言有很多种，
        self.assertEqual(200, req.status_code)
        self.assertLessEqual(req.elapsed.total_seconds(),3)
        # assert 'George' == req_json_data[0]['first_name']
        # assert 'emma.wong@reqres.in' in req_json_data[2]['email']

    # 不执行的测试跳过
    @unittest.skip
    def test_post_01(self):
        print('post方法')

if __name__ == '__main__':
    # python 文件名方式执行 在终端执行
    # unittest.main()
    # 建立一个套件，将测试用例组合集合
    now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
    suite = unittest.TestSuite()
    # 将测试用例加入套件中，使用testloader加入
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(unitDemoTest))
    # 运行并生成html的报告
    report_path=os.path.join(os.path.dirname(__file__),'report')
    filename=report_path+"/"+now+"_result.html"
    with open(filename,'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='测试报告',
            description='接口测试用例')
        runner.run(suite)