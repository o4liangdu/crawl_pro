# -*- coding: utf-8 -*-
# 处理item
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DemoPipeline(object):
    def process_item(self, item, spider):
        return item

