# -*- coding: utf-8 -*-
from ITcast.items import ItcastItem
import scrapy

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['http://www.itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        #pass
        #print(response.body)
        node_list = response.xpath("//div[@class='li_txt']")
        for node in node_list:
            item=ItcastItem()
            name=node.xpath("./h3/text()").extract()
            title=node.xpath("./h4/text()").extract()
            info=node.xpath("./p/text()").extract()

            item['name']=str(name[0])
            item['title']=str(title[0])
            item['info']=str(info[0])
            yield item