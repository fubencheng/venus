#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------
 @file: BaseHandler
 @description: 
 @author: fubencheng
 @create: 2018-04-18 16:06
------------------------------------------------------
"""

from tornado.web import RequestHandler


class BaseHandler(RequestHandler):

    def __init__(self, application, request, **kwargs):
        RequestHandler.__init__(self, application, request, **kwargs)

    def data_received(self, chunk):
        pass


if __name__ == '__main__':
    pass
