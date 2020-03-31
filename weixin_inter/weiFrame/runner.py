import sys
import logging
import os
import pytest

# sys.path.append(os.path.dirname(sys.modules[__name__].__file__))
from weiFrame.init import sysconfig

fileHandler = logging.FileHandler(filename="../weiFrame/log/auto.log",encoding="utf-8")
logging.getLogger().setLevel(0)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
fileHandler.setFormatter(formatter)

logging.getLogger().addHandler(fileHandler)


if __name__ == '__main__':
    logging.info("开始执行测试用例")
    pytest.main(['-sq', '/Users/lindafang/PycharmProjects/weixin_inter/weiFrame/testcases/department/test_creat_depart.py'])
    logging.info("测试用例结束")
'''
通讯录同步开启，API编辑通讯录
'''