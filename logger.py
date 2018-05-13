#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------
 @file: config.py
 @description:
 @author: fubencheng
 @create: 2018-04-28 21:04
------------------------------------------------------
"""

import logging
logging.basicConfig()

from logging.handlers import RotatingFileHandler
import os

def log_setting(name="", level=logging.DEBUG, stdout_switch=True):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not len(logger.handlers):
        log_path = os.path.normpath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "."))
        log_dir = os.path.join(log_path, "logs")
        if not os.path.isdir(log_dir):
                os.mkdir(log_dir)

        log_file_name = os.path.join(log_dir, name + ".log")

        # 定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
        file_handler = RotatingFileHandler(log_file_name, maxBytes=10 * 1024 * 1024, backupCount=5)
        file_handler.setLevel(level)

        # 创建一个控制台handler，该handler用于把DEBUG及以上级别日志输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

         # 定义handler的输出格式
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s %(process)d:%(thread)d(%(threadName)s) - [%(funcName)s: %(filename)s,%(lineno)d] - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 给logger添加handler
        logger.addHandler(file_handler)
        if stdout_switch:
            logger.addHandler(console_handler)
    return logger

log = log_setting(name="charts", level=logging.INFO)