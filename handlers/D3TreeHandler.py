#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------
 @file: TreesHandler
 @description: 
 @author: fubencheng
 @create: 2018-04-19 14:45
------------------------------------------------------
"""

from tornado.web import RequestHandler
import logger

# treeData = {"name": "http:/getuserinfo","children": [{"name": "http:/findnameandcountrybyid","children": [{"name": "http:/findgenderbyid","children": [{"name": "http:/querynamebyuserid","size": 3938}]}]}]}

source = [
    {"name": "http:/getuserinfo", "id": "1", "parentId": "0"},
    {"name": "http:/findnameandcountrybyid", "id": "2", "parentId": "1"},
    {"name": "http:/findgenderbyid", "id": "3", "parentId": "2"},
    {"name": "http:/querynamebyuserid", "id": "4", "parentId": "2"},
    {"name": "java", "id": "5", "parentId": "2"},
    {"name": "python", "id": "6", "parentId": "1"},
    {"name": "go", "id": "7", "parentId": "6"},
    {"name": "javascript", "id": "8", "parentId": "6"},
]

class D3TreeHandler(RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.render("d3tree.html")


class D3TreeDataHandler(RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        logger.get_logger('d3tree').info(self.get_tree_data())
        tree_data_obj = self.get_tree_data()
        display = self.get_argument("display")
        if int(display) == 1:
            self.write(tree_data_obj[0])
        else:
            self.write({})

    def get_tree_data(self, _id = "0"):
        tree_data = []
        for item in source:
            if item["parentId"] == _id:
                tree_data.append({"id": item["id"], "name": item["name"], "children": self.get_tree_data(item["id"])})
        return tree_data

if __name__ == '__main__':
    pass
