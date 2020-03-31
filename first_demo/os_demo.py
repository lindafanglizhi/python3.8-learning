import os


# 输入是当前路径 f  function函数
# print(os.getcwd())
# # v 变量没有括号
# print(os.curdir)
# # 后面的文件 所在的文件夹名称
# print(os.path.dirname("/Users/lindafang/PycharmProjects/first_demo/radom1_demo.py"))
# # 以列表形式把文件名显示出来
# print(os.listdir("/Users/lindafang/PycharmProjects/first_demo"))
# os.mkdir("/Users/lindafang/PycharmProjects/first_demo/dirss")
# print(os.path.isdir("/Users/lindafang/PycharmProjects/first_demo/dirss"))
# print(os.path.isfile("/Users/lindafang/PycharmProjects/first_demo/dirss"))
# 获得当前所有文件夹的名称与某一个文件名组合在一起。__file__表示当前文件
# print(os.path.join(os.path.dirname(__file__), 'demo_2.py'))

# 写一个函数，接受一个参数，如果是文件，就执行这个文件，如果是文件夹，就执行这个文件夹下所有的py文件
os.system('ping 127.0.0.1')