from datetime import datetime
import time

dt = datetime.now()  # 创建一个datetime类对象
print(dt.year, dt.month, dt.day)
print('时间: ', dt.strftime('%Y-%m-%d %H:%M:%S %f'))
print('今天是这周的第%s天 ' % dt.strftime('%w'))
print('今天是当月的第%s天 ' % dt.strftime('%d'))
time.sleep(1)#休眠，秒为单位
print(time.time())
#当前时间 秒
d1 = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(d1)
