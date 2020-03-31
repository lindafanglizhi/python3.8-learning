
# 打开文件，以读的方式
# f = open('data.txt', 'r')
# # 读一行
# data_line = f.readline()
# # 读多行，是在上面读的后面开始读的，一定有个指针的东西
# # 移动到文件开始
# f.seek(0)
# data_lines = f.readlines()
# print(data_lines)


# wf=open('data.txt','a')
# w_date =wf.write("\n这是后加的")
# wf.close()

with open('data.txt', 'r') as file:
    data=file.read()

print(data)