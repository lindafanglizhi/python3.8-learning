
try:
    # 要执行的代码可能出错的放这
    with open('data.json', 'r') as f:
        data_json = f.read()
        print(data_json)
except:
    # 出错时要进行代码放在这
    print("看看文件是否存在")
finally:
    # 不管是否出错都执行的结果收尾的代码写这
    print("结束了")

