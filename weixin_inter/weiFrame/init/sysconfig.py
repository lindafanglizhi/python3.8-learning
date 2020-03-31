#! /usr/bin/env python
#coding=utf-8

import configparser
import logging

def read_config(cfg_file):
    cfg = configparser.ConfigParser()
    cfg.read(cfg_file)
    return cfg



sys_cfg = read_config('/Users/lindafang/PycharmProjects/weixin_inter/weiFrame/config/common.cfg')


if __name__=="__main__":
    cfg=read_config("/Users/lindafang/PycharmProjects/weixin_inter/weiFrame/config/common.cfg")
    print(cfg.get('contact_para','create_dep_url'))


