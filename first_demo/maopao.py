list1 = [1, 3, 5, 7, 9, 2, 4, 8, 10]


def Sort(list1):
    for i in range(len(list1) - 1):
        for j in range(len(list1) - i - 1):
            if list1[j] > list1[j + 1]:
                # 交换位置
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    return list1


print(Sort(list))
