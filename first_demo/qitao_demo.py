count = 88


def a():
    count = 12
    # print(count)

    def b():
        # count = 10
        print(count)

    b()  # 如果在函数体内不调用内嵌的函数，那么无法在外部调用
    # return count

a()
