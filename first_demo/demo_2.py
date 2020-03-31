# tuple = ('python', 12, 35.8, 888)
# 不能添加，不可变
# # 长度
# print(len(tuple))
# #  类型
# print(type(tuple))
# # tuple.index(12, 1, 3)
# # 是第几个索引
# print(tuple.index(35.8))

my_dict = {'name': 'linda', 'age': 18, 'hair': 'black'
           }
# print(type(my_dict))
# print(len(my_dict))
# my_dict.copy()
# copy没结果？？
# print(my_dict.pop('hair'))
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.get('name'))
# print(my_dict.get('age'))
# print(my_dict['name'])
# # print(my_dict)
# print(my_dict.items())
# my_dict['hobby'] = 'taiji'
# print(my_dict)
# del my_dict['hobby']
# print(my_dict)
#
# for key in my_dict:
#     print(key, '-->', my_dict[key])
#
# for value in my_dict.values():
#     print(value)
#
# for key, value in my_dict.items():
#     print(key, ':', value)
    # 断言 前面与后面的值是不是相等，如果相等返回true
    # assert my_dict[key] == value+'1'
#
my_set ={1,2,3}
# 不能重复,没有顺序
# my_set.add(4)
# print(my_set)
# my_set.add(3)
# print(my_set)
# 集合，交集，并集，叉集
my_set1={2,3,5,6}
# print('交集是:%s' % my_set.intersection(my_set1))
# print(my_set.difference(my_set1))
# # 删除1这个元素
# print(my_set.discard(1))
# print(my_set)
print('并集是:%s 子集是%s' % (my_set.union(my_set1),my_set1.issubset(my_set)))
print('是子集吗？:%s' % my_set1.issubset(my_set))
# print(str(my_dict))
# dict_str =str(my_dict)
list1 =list(my_dict.values())
print(list1[0])
list1.append('linda')
print(list1)
# 去重
print(list(set(list1)))
