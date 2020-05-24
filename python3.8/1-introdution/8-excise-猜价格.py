# Author: lindafang
# Date: 2020-05-22 12:44
# File: 8-excise-猜价格.py
# 在1-500间随机产生一个整数，对商品猜价格：你从控制台输入信息
# 让用户猜，只提示，猜大了，猜小了，猜对结束。

# 随机数--只有一个所以不参与循环,输入的数多个在循环里
# if ,elif, else 三个结果
# while 循环 条件break
import random
goods_price = random.randint(1,500)


total=5
count=0
while True:
    # 键盘输入的数是字符串，不能直接与整数对比，需要强制转换为int
    my_price=int(input("输入你猜的价格："))
    if my_price<goods_price:
        print("猜小了")
    elif my_price>goods_price:
        print("猜大了")
    else:
        print("猜对了")
        break

# 如果只允许猜5次，可以加个判断条件if,需要提示用这个 ，也可在循环上加条件，无提示

    count +=1
    if count>=total:
        print(f"你猜了{count}次了")
        break
