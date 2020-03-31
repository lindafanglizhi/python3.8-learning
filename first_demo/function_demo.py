import time
import os


# 定义一个函数
def eat(name, age, sex='女'):
    print("我的名字： %s，年龄是%s,性别：%s" % (name, age, sex))

    return name

str=eat(name='linda',age=18)
# 调用一个函数
# str1=eat(*('linda',18,'女'))
# str1=eat(*['linda',18,'女'])
# str1 = eat(**{'name': 'linda', 'age': '88'})
# print(str1)

print(time.time())
time.sleep(5)
print(time.time())
# sum=lambda x, y : x+y
# print(sum(1,2))
print(os.getcwd())