from functools import reduce

# add是一个函数，返回加2，arr是个列表，map后，把列表中的每个元素都+2后返回列表
# add = lambda x:x+2
# arr = [1,2,3]
# print(list(map(add,arr)))
# #  add是个匿名函数，两个参数相加返回和。arr1,arr2两个列表，
# #  map后，是将列表中每一个相同位置的元素执行相加操作。
# add = lambda x,y:x+y
# arr1 = [1,2,3]
# arr2 = [4,5,6]
# print(list(map(add,arr1,arr2)))
# # 若arr1与arr2不对等情况
# add = lambda x,y:x+y
# arr1 = [1,2,3,4]
# arr2 = [4,5,6]
# print(list(map(add,arr1,arr2)))
# zip的意思将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象
# 我们可以使用 list() 转换来输出列表。
# # 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
# print(list(zip(arr1,arr2)))
# a1,a2 =zip(*zip(arr2,arr1))
# print(list(a1))
#
#
# # ***将元组转换成list***
# print(list(map(int, (1, 2, 3))))
# # ***将字符串转换成list***
# print(list(map(int, '1234')))
# # ***提取字典的key，并将结果存放在一个list中***
# print(list(map(int, {1:2,2:3,3:4})))
# # ***字符串转换成元组，并将结果以列表的形式返回***
# print(tuple(map(tuple, 'agdf')))
# #将小写转成大写
# def u_to_l (s):
#   return s.upper()
#
# print(list(map(u_to_l,'asdfd')))
#
#
#
# def add100(x):
#     return x+100
# hh = [11,22,33]
#
# print(list(map(add100,hh)))
# print([(i+100) for i in hh])
#
#
# def abc(a, b, c):
#     return a*10000 + b*100 + c
#
# ss = [11,22,33]
# dd = [44,55,66]
# ff = [77,88,99]
# print(list(map(abc,ss,dd,ff)))
#
# ll=list(map(lambda x: x % 2, range(7)))
# print(ll)

# filter是过滤，将后面的每一个元素通过前面的函数过滤，满足的留下。
a=[1,2,3,4,5,6,7,8,9]
# print(list(filter(lambda x: x%2==0, a)))

# py3中reduce函数要导入
# from functools import reduce
# reduce函数，reduce函数会对参数序列中元素进行累积。
print(reduce(lambda x, y: x+y,a,10))
print(reduce(lambda x, y: x*y,a))
# 求1-100的和
print(reduce(lambda x, y: x+y,range(1,101)))