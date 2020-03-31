def outer(func):
    print("开始装饰")

    def inner(username,password):
        print("----开始测试了---")
        res =func(username,password)
        print("----结束测试了---")
        return res

    return inner

# outer  --test_1--->outer(test_1)--->inner---test_1
# 测试方法以test开头可以直接执行

@outer
def test_1(username,password):
    print("----测试登陆----")
    print("你的名字%s,密码是%s" %(username,password))
    return "登陆成功！"


print(test_1('linda', '888888'))

