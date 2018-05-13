#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------
 @file: router.py
 @description: 
 @author: fubencheng
 @create: 2018-04-18 17:41
------------------------------------------------------
"""

from handlers.IndexHandler import IndexHandler
from handlers.TablesHandler import TablesHandler
from handlers.D3TreeHandler import D3TreeHandler, D3TreeDataHandler
from handlers.JqueryTreeHandler import JqueryTreeHandler

URL_MAPPING = [(r"/", IndexHandler),
               (r"/tables", TablesHandler),
               (r"/d3tree", D3TreeHandler),
               (r"/d3tree/data", D3TreeDataHandler),
               (r"/jquerytree", JqueryTreeHandler)]

if __name__ == '__main__':
    pass