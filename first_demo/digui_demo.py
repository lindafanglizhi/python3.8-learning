# 1-n和
# 这是求和

def sum_number(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(sum_number(100))

# 递归是自己调用自己，相当循环了。不用写循环。
def sum_num_digui(n):
    if(n<=0):
        return 0
    return sum_number(n-1)+n

# n=f(n)-f(n-1)
print(sum_num_digui(100))


