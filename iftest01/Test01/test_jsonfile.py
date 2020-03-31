import unittest
import requests
from ddt import ddt, file_data, unpack


'''
https://reqres.in/api/users
{
    "name": "morpheus",
    "job": "leader"
}
'''


@ddt
class TestDdtForJson(unittest.TestCase):
    def setUp(self):
        self.url = 'https://reqres.in/api/users'

    @file_data('test_data.json')
    def test_IF_Post_Create(self, **value):
        # print(type(value))
        # print(value)
        req = requests.post(url=self.url, data=value)
        print(req.json())
        self.assertEqual(req.status_code, 201)
        self.assertEqual(req.json()['name'], 'morpheus')


if __name__ == '__main__':
    unittest.main()

