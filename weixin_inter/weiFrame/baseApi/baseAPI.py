import requests
import logging
from weiFrame.init.sysconfig import sys_cfg


class BaseApi:
    def __init__(self):
        logging.info("init base api interface")
        self.cop_id = sys_cfg.get('corp_para', 'corp_id')
        self.token_url = sys_cfg.get('corp_para', 'token_url')
        self.res = ''

    def get_token(self, secret):
        # secret是通讯录中的
        params = {'corpid': self.cop_id, 'corpsecret': secret}
        # logging.info('params'+str(params))
        # logging.info('token_url:'+self.token_url)
        token_res = requests.get(self.token_url, params=params)

        return token_res.json().get('access_token')

    def post_json(self, url, json_obj, params=None):
        if params:
            self.res = requests.post(url, json=json_obj, params=params)
        else:
            self.res = requests.post(url, json=json_obj)

    def get_response(self):
        return self.res.json()




