import requests
# RESTAPI restful风格


def get_page():
    url='https://reqres.in/api/users?page=1'
    # url=''
    # 参数形式，关键字url=value,
    req = requests.get(url=url)
    # print(req.json()['data'][0]['first_name'])
    # 因为断言data多次，只想返回一次数据，把data返回放到req_json_data变量中
    req_json_data=req.json()['data']
    # 判断 返回数据中第一个数据里的名字叫George
    assert 'George' == req_json_data[0]['first_name']
    # 判断 返回数据中第3个的email包含（in）tobias.funke
    assert 'emma.wong@reqres.in' in req_json_data[2]['email']


# get_page()

def post_create_user():
    url = 'https://reqres.in/api/users'
    data = {
        'name': 'linda',
        'job': 'leader'
    }
    req = requests.post(url=url, data=data)
    # print(req.json())
    # print(req.status_code)
    # 首先断言http协议层返回响应状态码
    assert 201 == req.status_code
    # 其次断言业务数据层的返回数据是否正确
    assert 'linda' == req.json()['name']
#     最后通常断言性能层面的时间是否满足用户要求
    print(req.elapsed.total_seconds())
    assert req.elapsed.total_seconds()<=3


# post_create_user()

def put_edit_user():
    url = 'https://reqres.in/api/users/2'
    data = {
        'name': 'linda888',
        'job': 'leader'
    }
    req = requests.put(url=url, data=data)
    assert 200 == req.status_code
    assert 'linda888' == req.json()['name']

# put_edit_user()


def delete_user():
    url = 'https://reqres.in/api/users/2'
    req = requests.delete(url=url)
    assert 204 == req.status_code


# delete_user()
# url = 'https://reqres.in/api/users/2'
# req = requests.request(method='delete', url=url)
# print(req.status_code)
