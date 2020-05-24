# Author: lindafang
# Date: 2020-05-22 13:30
# File: 8-excise-猜拳.py

list1=["草","火","水"]


import random

total=3
count=0
while True:
    computer = random.randint(0,2)
    print(computer)
    my_choice=int(input("输入你猜的0c,1h,2s："))
    if (my_choice,computer) in [(0,1),(1,2),(2,0)]:
        print("我输了"+list1[my_choice])
    elif (my_choice,computer) in [(1,0),(2,1),(0,2)]:
        print("你输了"+list1[my_choice])
    else:
        print("平局了")


# 如果只允许猜5次，可以加个判断条件if,需要提示用这个 ，也可在循环上加条件，无提示

    count +=1
    if count>=total:
        print(f"你猜了{count}次了")
        break