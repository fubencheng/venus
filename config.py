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

import os
import sys
import yaml
from yaml.parser import ParserError

BASE_DIR = os.path.dirname(__file__)

class Config(object):
    def __init__(self):
        self.config_path = os.path.join(BASE_DIR, 'conf.yaml')

    def get_config(self):
        if not os.path.exists(self.config_path):
            print "config file not exist"
            sys.exit(1)
        config_file = open(self.config_path)
        try:
            config = yaml.load(config_file)
            return config
        except ParserError as e:
            print "parse config.yaml error"
            print e
            sys.exit(1)

if __name__ == '__main__':
    print Config().get_config();