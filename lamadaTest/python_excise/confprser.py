# 使用配置文件来灵活的配置,在python使用
# configParser解析的配置文件；
# 文件中由多个section构成，每个section下又有多个配置项

'''
[section0]

key0 = value0
key1 = value1

[section1]

key2 = value2
key3 = value3
'''

import configparser
import os
curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "secion.ini")
print(cfgpath)  # cfg.ini的路径

# 创建管理对象
conf = configparser.ConfigParser()

# 读ini文件
conf.read(cfgpath)

# 获取所有的section---查询
sections = conf.sections()

print(sections)  # 返回list

items = conf.items('section0')
print(items)  # list里面对象是元祖

# 添加一个select
conf.add_section("emali_tel")
print(conf.sections())

# 往select添加key和value
conf.set("emali_tel", "sender", "linda@tel.com")
conf.set("emali_tel", "port", "265")
items = conf.items('emali_tel')
print(items)  # list里面对象是元祖

conf.write(open(cfgpath, "a"))  # 追加模式写入


# 删除一个 section中的一个 item（以键值KEY为标识）
conf.remove_option('section0', "name")

items = conf.items('section0')
print(items)  # list里面对象是元祖

# 删除一个 section
conf.remove_section('section0')
sects = conf.sections()
print(sects)  # list里面对象是元祖


