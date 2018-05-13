#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------
 @file: TablesHandler
 @description: 
 @author: fubencheng
 @create: 2018-04-19 11:31
------------------------------------------------------
"""

from tornado.web import RequestHandler

class TablesHandler(RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.render("tables.html")

if __name__ == '__main__':
    print "TablesHandler module init"
    pass