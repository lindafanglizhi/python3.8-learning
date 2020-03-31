import random

# random.seed(8)   #随机种子
print(random.random())  # [0,1)
print(random.uniform(3, 1))
# [1,3] 小数
print(random.randint(1, 10))
# [1,10]  a<b  整数
print(random.randrange(1, 10, 2))
# [1,10,2]步长为2，就是奇数
print(random.choice("asdfghjkl"))
# 从字符串，元组，列表中随机提取一个元素
s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(s)  # 打乱
print(s)
print(random.sample(s, 3))
# 从s中随机获取3个值
