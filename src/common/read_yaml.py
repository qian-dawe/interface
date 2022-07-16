#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Interface
@File    ：read_yaml.py
@IDE     ：PyCharm
@Date    ：2022/7/9 14:13
"""
import yaml


class ReadYaml:

    # 读取
    @staticmethod
    def read_yaml(yaml_path):
        with open(yaml_path, 'r', encoding="utf-8") as f:
            value = yaml.load(f.read(), Loader=yaml.FullLoader)
            return value

    # 写入
    @staticmethod
    def write_yaml(yaml_path, data):
        with open(yaml_path, 'w', encoding="gb2312") as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    # 清除
    @staticmethod
    def clear_yaml(yaml_path):
        with open(yaml_path, 'w', encoding="gb2312") as f:
            f.truncate()
