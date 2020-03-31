def dive(num1,num2):
    return num1/num2

try:
    print(dive(5, 'a'))
except ZeroDivisionError:
    print("除0了")
except TypeError:
    print("你输入的不是数字")
except:
    print("有其他问题吧")
else:
    print("没有什么错了")
finally:
    print("计算完成了")

