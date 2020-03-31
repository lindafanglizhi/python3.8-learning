import time
from datetime import datetime

# print(time.time())
# # 中断2秒
# time.sleep(2)
# print(time.time())

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
dt =datetime.now()
print(dt)
print(dt.year,dt.month,dt.day)
print('时间：',dt.strftime("%Y-%m-%d"))
# %w是表示今天是这周的第几天，其他表示可以上网查
print("今天是这周的第%s天" % dt.strftime('%w'))



