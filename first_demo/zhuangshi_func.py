# def outer(func):
#     print("开始装饰")
#
#     def inner():
#         print("------验证------")
#         func()
#         print("------日志------")
#
#     return inner
#
# @outer   #  test = outer(test)  ==> test = inner
# def test():
#     print("------test登录------")
# test()



# # 要被装饰的函数，有参数，没有返回值
# def outer(func):
#     print("开始装饰")
#     def inner(username,password):
#         print("------验证------")
#         func(username,password)
#         print("------日志------")
#     return inner
# #装饰器
# @outer   #  test = outer(test)  ==> test = inner
# def test(username,password):
#     print("------test登录------",username,password)
# test("张三","123")


# # 要被装饰的函数，没有参数，有返回值
# def outer(func):
#     print("开始装饰")
#     def inner():
#         print("------验证------")
#         print("------日志------")
#         return func()
#     return inner
# #装饰器
# @outer   #  test = outer(test)  ==> test = inner
# def test():
#     print("------test登录------")
#     return "登录成功\n"
# print(test(),"---------")


# 要被装饰的函数，有参数，有返回值

def outer(func):
    print("开始装饰")
    def inner(a):
        print("------验证------")
        print("------日志------")
        return func(a)
    return inner
#装饰器
@outer   #  test = outer(test)  ==> test = inner
def test(a):
    print("------test登录------",a)
    return "登录成功"
print(test("你好"),"---------")




# 多个装饰器
# 运行顺序：从下到上
def val(func):
    print("开始装饰验证val")
    def inner():
        print("------验证------")
        func()
    return inner

def log(func):
    print("开始装饰日志log")
    def inner():
        func()
        print("------日志------")
    return inner
#装饰器
@log
@val   #  test = outer(test)  ==> test = inner
def test():
    print("------test登录------")
test()