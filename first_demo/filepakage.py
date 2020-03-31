import os
# os.mkdir("/Users/lindafang/PycharmProjects/first_demo/newdir/ss")  #创建文件夹"d:/ss"
# print(os.getcwd())   #获取当前目录
# print(os.listdir("/Users/lindafang/PycharmProjects/first_demo"))  #获取目录列表"d:/"
# os.rmdir("/Users/lindafang/PycharmProjects/first_demo/newdir")  #删除文件夹"e:/ss"
base_path = "/Users/lindafang/PycharmProjects/first_demo/newdir"
files = os.listdir(base_path)  #["a","b"]
print(files)
print(os.path.join(base_path,'ss'))
print(os.path.isfile('/Users/lindafang/PycharmProjects/first_demo/newdir/sfsf.py'))


def remove_file(base_path):
    list_file = os.listdir(base_path)
    if len(list_file) == 0:
        os.rmdir(base_path)
    for file_str in list_file:
        file = os.path.join(base_path,file_str)
        if os.path.isfile(file):
            os.remove(file)
        else:
            list_file = os.listdir(file)
            if len(list_file) == 0:
                os.rmdir(file)
            else:
                remove_file(file)





#
# import os
# for root, dirs, files in os.walk("e:/s", topdown=False):
#     for name in files:
#         os.remove(os.path.join(root, name))
#     for name in dirs:
#         os.rmdir(os.path.join(root, name))