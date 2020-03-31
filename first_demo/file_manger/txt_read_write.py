
# f=open('data.txt','r')
# 读一行，返回字符串
# data_line =f.readline()
# 读多行，返回列表
# data_lines =f.readlines()
# print(data_lines)
# 读全部
# data =f.read()
# print(data)
# data1=f.read()
# print(data1)
# f.seek(0)
# print(f.read())

w = open('data.txt','a')
w.writable()
w.write("这是追加的中文")


with open('data.txt','r') as f:
    new_data =f.read()


print(new_data)