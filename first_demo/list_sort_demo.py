list1 = [1, 5, 3, 7, 9, 4, 6]
list2 = ['d', 'g', 'u', 's', 'l', 'a']
list_tuple = [
    ('join', 'A', 15),
    ('jane', 'B', 12),
    ('linda', 'B', 10),
]


# str_sort=sorted("This is a test string from Linda".split(), key=str.lower)
# str_sort = sorted("This is a test string from Linda".split())
# print(str_sort)

# ASCII码  a:97?  A:65   a-z:97-122,A-Z:65-90,0-9:48-57。

# list_tuple.sort()
# print(list_tuple)
# key
print(sorted(list_tuple,key=lambda list:list[2],reverse=True))
