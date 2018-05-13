#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------
 @file: JqueryTreeHandler
 @description: 
 @author: fubencheng
 @create: 2018-04-20 10:39
------------------------------------------------------
"""

from tornado.web import RequestHandler

class JqueryTreeHandler(RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.render("jquerytree.html")

if __name__ == '__main__':
    pass