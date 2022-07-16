#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import logging
import traceback
import unittest
from pathlib import Path
from time import sleep
import ddt
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from src.common.logs import log
from src.common.read_yaml import ReadYaml
from src.common.requests_method import Requests
from basePage.base import Common
from src.common.encryptionEecryption import get_md5
from src.common.ParseExcel import ParseExcel, ReadExcel
excelPath = "D:\\PycharmProject\\interface\\src\\data\\data.xlsx"
sheetName = u"Sheet1"
# excel = ParseExcel(excelPath, sheetName)
file = Path(Path(__file__).parent.parent, 'src/data/api_case.xlsx')
api_case_path = Path(Path(__file__).parent.parent, 'src\\data\\api_case.yaml')
case_path = Path(Path(__file__).parent.parent, 'src\\data\\case.yaml')
excel = ReadExcel(file)


# class Test01(object):
#
#     # def setUp(self) -> None:
#     #     self.run = RequestsMethod()
#
#     @pytest.mark.parametrize('caseInfo', ReadYaml.read_yaml(case_path))
#     def test_01(self, caseInfo):
#         url = caseInfo['url']
#         method = caseInfo['method']
#         data = caseInfo['data']
#         res1 = Requests().run_requests(url, method, data)  # post方法需要穿入json格式的参数
#         if res1['pub']['status'] == 4:
#             print("成功")
#         else:
#             print("失败")
#
#
# # @ddt.ddt
# class Test02(object):
#
#     @pytest.mark.parametrize('caseInfo', ReadYaml.read_yaml(api_case_path))
#     def test_01(self, caseInfo):
#         name = caseInfo['name']
#         url = caseInfo['url']
#         method = caseInfo['method']
#         data = caseInfo['data']
#         print('md5:' + get_md5(caseInfo['data']['username']))
#         expect = caseInfo['expect']
#         res = Requests().run_requests(url, method, data)
#         if res == expect:
#             print(f"用例名称：{name},实际结果与期望结果一致")
#         else:
#             print(f"用例名称：{name},实际结果与期望结果不一致，响应结果：{res}")


class Test03(object):
    def test_01(self):
        for i in range(2, excel.get_rows() + 1):
            print(excel.get_value(i, 7))
            if excel.get_value(i, 7) == "是":
                caseName = excel.get_value(i, 2)
                url = excel.get_value(i, 3)
                method = excel.get_value(i, 4)
                params = excel.get_value(i, 5)
                if params is not None:
                    data = json.loads(params)
                    print(f'参数：{data}')
                    expect_result = excel.get_value(i, 8)
                    res = Requests().run_requests(method, url, data)
                    excel.write_value(i, 9, str(res))
                    print(f"测试用例:{caseName}, url:{url}, 期望结果:{expect_result}, 实际结果:{res}")
                    if str(res) == expect_result:
                        print("实际结果与期望结果一致")
                    else:
                        print("实际结果与期望结果不一致")
                else:
                    expect_result = excel.get_value(i, 8)
                    res = Requests().run_requests(method, url, data=None)
                    excel.write_value(i, 9, str(res))
                    print(f"测试用例:{caseName}, url:{url}, 期望结果:{expect_result}, 实际结果:{res}")
                    if str(res) == expect_result:
                        print("实际结果与期望结果一致")
                    else:
                        print("实际结果与期望结果不一致")
            else:
                pass


'''
@ddt.ddt
class Test02(unittest.TestCase):

    def setUp(self) -> None:
        self.run = RunMain()

    # def validate(self, expect, actual):
    #     for key, value in expect.items():
    #         if key in actual:
    #             self.assertEqual(value, actual[key])
    #         else:
    #             for _key, _value in actual.items():
    #                 if isinstance(_value, dict) and (key in _value):
    #                     expect_new = {}
    #                     expect_new[key] = value
    #                     self.validate(expect_new, _value)

    # @pytest.mark.smoke
    @ddt.file_data(yaml_path)
    def test_01(self, **kwargs):
        url = kwargs['url']
        method = kwargs['method']
        data = kwargs['data']
        res1 = self.run.run_main(url, method, data)  # post方法需要穿入json格式的参数
        print(res1)
        # self.validate(kwargs['validate'], res1)
        for key, value in kwargs['expect'].items():
            print(key, value, res1[key])
            if key in res1:
                self.assertEqual(value, res1[key])
'''

if __name__ == '__main__':
    unittest.main()
