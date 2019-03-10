# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo
from Tencent.settings import mongo_db_collection,mongo_db_name,mongo_host,mongo_port

import os

class TencentPipeline(object):
    def __init__(self):
        #self.f=open("guangzhou.json","w")
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        sheetname = mongo_db_collection
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item

    def close_spider(self,spider):
        #self.f.close()
        pass
