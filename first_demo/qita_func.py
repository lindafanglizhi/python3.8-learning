import sys
import subprocess
import re
import shutil
import json
# print(sys.platform)

# subprocess.call('ping 127.0.0.1',shell=True)

# shutil.copy('/Users/lindafang/PycharmProjects/first_demo/digui.py', '/Users/lindafang/PycharmProjects/first_demo/digui1.py')
prog = re.compile('\d{2}')  # \d是表示数字，{2}2个数字 \d{2}
print(prog.search('adb12dfef34skjf788').group())
# 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。
print(prog.findall('adb12dfef34skjf788'))

dict ={
    'name':'linda',
    'age':18,
    'live':True,
    'love':None
}

json_str =json.dumps(dict)
print(json_str)
print(json.loads(json_str))