#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import logging
from pathlib import Path

log = logging
log_path = Path(Path(__file__).parent.parent.parent, 'src//log//run_case.log')
# 设置日志输出格式
log.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                filename=log_path,
                datefmt='%Y-%m-%d %H:%M:%S',
                filemode='w')
