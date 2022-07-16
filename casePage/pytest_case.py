#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：test 
@File    ：pytest_case.py
@IDE     ：PyCharm 
@Date    ：2022/2/19 17:16 
"""
import pytest


class Test01:

    # ids是用例名称
    @pytest.mark.parametrize('args', ['张三', '李四', '王五'], ids=["用例1", "用例2", "用例3"])
    def test_01(self, args):
        print(f"输出数据{args}")

    @pytest.mark.smoke()
    def test_02(self):
        print("执行冒烟用例分组")


class Test02:

    def test_01(self):
        print("用例1")


if __name__ == '__main__':
    pytest.main()
