import allure
import pytest

# 这个是要测试的方法，step是测试步骤
@allure.step("测试步骤1：字符串相加：{0},{1}")
def str_add(str1,str2):
    print("hello")
    if not isinstance(str1,str):
        return "%s 不是字符串" % str1
    if not isinstance(str2,str):
        return "%s 不是字符串" % str2
    return str1+str2


@allure.severity("critical")
@allure.feature("这是测试某个功能")
@allure.story("测试模块")
@allure.issue("bug编号：043")
@allure.testcase("测试用例：测试字符串相加")
@pytest.mark.parametrize("para_one,para_two",[("hello","world"),
                                              ('4','8'),
                                              ('我','喜欢'),
                                              (4,True)
                                              ],ids=["test string",
                                                     "test number",
                                                     "test unicode",
                                                     "test error"])
def test_case(para_one,para_two):
    # 调用函数，获得返回
    res =str_add(para_one,para_two)
    # 类似在报告中print
    allure.attach("add返回结果","{0}".format(res))
    with allure.step("测试步骤2,结果校验{0}=={1}".format(res,para_one+para_two)):
        assert res ==para_one+para_two, res
