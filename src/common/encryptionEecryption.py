#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import hashlib


# md5加密
def get_md5(text):
    # 1.示例化md5加密对象
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
