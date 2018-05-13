#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------
 @file: IndexHandler
 @description: 
 @author: fubencheng
 @create: 2018-04-18 16:22
------------------------------------------------------
"""

from BaseHandler import BaseHandler

class IndexHandler(BaseHandler):

    def get(self):
        self.render("index.html")


if __name__ == '__main__':
    pass