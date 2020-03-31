# 定义一个全局变量，注意它的位置 和 命名格式
gl_name = "hello"


def change_name():
    # 对全局变量进行修改
    global gl_name
    gl_name = "world"


def main():
    print(gl_name)
    change_name()
    print(gl_name)


if __name__ == '__main__':
    main()