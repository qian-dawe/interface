#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：test 
@File    ：requests_method.py
@IDE     ：PyCharm 
@Date    ：2022/2/8 19:09 
"""
import requests
from src.common.logs import log


class Requests:

    def __init__(self):
        self.session = requests.session()

    def send_get(self, url, data, header=None):
        if header:
            return self.session.get(url=url, params=data, headers=header).json()
        else:
            return self.session.get(url=url, params=data).json()

    def send_post(self, url, data, header=None):
        if header:
            return self.session.post(url=url, params=data, headers=header).json()
        else:
            return self.session.post(url=url, params=data).json()

    def run_requests(self, method, url, data):
        res = None
        if method.lower() == 'get':
            res = self.send_get(url, data)
        elif method.lower() == 'post':
            res = self.send_post(url, data)
        else:
            log.warning("请求方法错误")
        return res

    # def http_request(self, method, _data=None, files=None, headers=None):
    #     if headers:
    #         for key, value in headers.items():
    #             self.headers[key] = value
    #             print(self.headers[key])
    #         if _data:
    #             if isinstance(_data, dict):
    #                 import json
    #                 _data = json.dumps(_data)  # 字典转换成字符串
    #     method = method.upper()
    #     res = ''
    #     if method == 'GET':
    #         res = self.get(_data)
    #     elif method == 'POST':
    #         res = self.post(_data)
    #     elif method == 'DELETE':
    #         res = self.delete(_data)
    #     return res
