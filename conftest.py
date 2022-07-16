#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Interface 
@File    ：conftest.py
@IDE     ：PyCharm 
@Date    ：2022/2/19 18:39 
"""
import pytest


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


# @pytest.fixture(scope="class", autouse=True)
# def test():
#     print("前置操作")
#     yield
#     print("后置操作")
