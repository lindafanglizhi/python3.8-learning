# add是一个函数，返回加2，arr是个列表，map后，把列表中的每个元素都+2后,返回列表

# add = lambda x:x**2
# arr = [1,2,3]
# print(list(map(add,arr)))

#  add是个匿名函数，两个参数相加返回和。arr1,arr2两个列表，
#  map后，是将列表中每一个(相同)位置的元素执行(相加)操作。

# add = lambda x,y:x+y
arr1 = [1,2,3]
arr2 = [4,5,6]
# print(list(map(add,arr1,arr2)))
# 若arr1与arr2不对等情况
# add = lambda x,y:x+y
# arr1 = [1,2,3,4]
# arr2 = [4,5,6]
# print(list(map(add,arr1,arr2)))
# 打包,将对应的元素打包成一个元组
# zip_ar=(zip(arr1, arr2))
# # 解压缩，解包，使用*将元组
# a1,a2=zip(*zip_ar)
# print(list(a1))
# 可以将元组转成list
# print(list(map(int, (1.5, 2, 3))))
# # 将字符串转成list
# print(list(map(int, '12345')))

# def add100(x):
#     return x+100
# hh=[11,22,33]
#
# print(list(map(add100, hh)))
# print(list(map(lambda x:x+100, hh)))
# print([(i + 100) for i in hh])

# filter是过滤 将每一个元素通过前面的函数过滤，满足的留下
a=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x % 2 == 0, a)))
from functools import reduce
# reduce函数，会对参数序列中的元素进行累积
#py3需要导入，from

print(reduce(lambda x, y: x + y, a,10))
# print(reduce(lambda x, y: x * y, a))
print(reduce(lambda x, y: x + y, range(1,101)))





