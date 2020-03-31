import sys
import os
import subprocess
import shutil
import re
# print(subprocess.call("ls"))
# print(subprocess.call("ping 127.0.0.1",shell=True))
# shutil.copy('/Users/lindafang/PycharmProjects/first_demo/demo_2.py',
#             '/Users/lindafang/PycharmProjects/first_demo/demo_4.py')
'''
\w	匹配字母数字及下划线
\W	匹配非字母数字及下划线
\s	匹配任意空白字符，等价于 [\t\n\r\f].
\S	匹配任意非空字符
\d	匹配任意数字，等价于 [0-9].
\D	匹配任意非数字
\A	匹配字符串开始
'''
prog=re.compile('\d{2}')   # \d是表示数字，{2}2个数字 \d{2}  *
print(prog.search('absdfsjfgdj23kgjsdflskj45sd').group())
# 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。
print(prog.findall('absdfsjfgdj23kgjsdflskj45sd'))
