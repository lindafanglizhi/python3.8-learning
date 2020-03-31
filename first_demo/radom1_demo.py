import random

# 产生是0-1之间小数
print(random.random())
# 整数
print(random.randint(1, 10))
# 2是步长，1，3，5
print(random.randrange(1, 20, 2))
# 从提供的字母中选择其中1个
print(random.choice("abcdeflkj"))
s=[1,2,3,4,5,6,7,8]
# 打乱
random.shuffle(s)
print(s)
# 样本取出3个
print(random.sample(s, 3))
