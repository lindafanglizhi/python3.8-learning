list = [1,4,2,6,7,9,23]
list1= ['f','h','e','c','a','z']
list.sort()
print(list)
print(sorted(list))
print(sorted(list1))
# list.sort()和sorted()函数增加了key参数来指定一个函数，此函数将在每个元素比较前被调用。
# 例如通过key指定的函数来忽略字符串的大小写

print(sorted("This is a test string from Andrew".split(), key=str.lower))
# key参数的值为一个函数，此函数只有一个参数且返回一个值用来进行比较。这个技术是快速的因为key指定的函数将准确地对每个元素调用。
# 更广泛的使用情况是用复杂对象的某些值来对复杂对象的序列排序
student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
print(sorted(student_tuples, key=lambda student: student[2],reverse=True))