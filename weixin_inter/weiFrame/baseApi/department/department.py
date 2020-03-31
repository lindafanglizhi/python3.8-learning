
import logging
from weiFrame.baseApi.baseAPI import BaseApi
from weiFrame.init.sysconfig import sys_cfg


'''
请求方式：POST（HTTPS）
请求地址：https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token=ACCESS_TOKEN

请求包体：

{
   "name": "广州研发中心",
   "parentid": 1,
   "order": 1,
   "id": 2
}
参数说明：

参数	必须	说明
access_token	是	调用接口凭证
name	是	部门名称。长度限制为1~32个字符，字符不能包括\:?”<>｜
parentid	是	父部门id，32位整型
order	否	在父部门中的次序值。order值大的排序靠前。有效的值范围是[0, 2^32)
id	否	部门id，32位整型，指定时必须大于1。若不填该参数，将自动生成id


'''


class DeptManagment(BaseApi):

    def __init__(self):
        BaseApi.__init__(self)
        logging.info("Init department management API")
        self.create_dep_url = sys_cfg.get('contact_para', 'create_dep_url')
        self.dep_secure = sys_cfg.get('contact_para', 'secure')

    def create_dept(self):
        new_part = {
                "name": "我的测试88",
                "parentid": 1,
                "order": 1
        }

        param = {'access_token': self.get_token(self.dep_secure)}
        # logging.debug("url:"+str(self.create_dep_url))
        # logging.debug("params:" + str(param))
        self.post_json(self.create_dep_url, new_part, params=param)

    def update_dept(self):
        pass

    def get_create_dept_res(self):
        return self.get_response()
