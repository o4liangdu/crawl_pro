# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['baidu.com']
    #start_urls = ['http://tencent.com/']
    baseURL="https://lvyou.baidu.com/shenzhen/remark/?rn=15&pn="
    endword="&style=hot#remark-container"
    offset=0
    start_urls = [baseURL+str(offset)+endword]

    def parse(self, response):
        node_list=response.xpath("//div[@class='remark-item clearfix']//div[@class='ri-remarktxt']")
        for node in node_list:
            item=TencentItem()
            # item['markLevel']=str(node.xpath("./td[1]/a/text()").extract()[0])
            # item['markText']=str(node.xpath("./td[1]/a/@href").extract()[0])
            # if len(node.xpath("./td[2]/text()")):
            #     item['positionType']=str(node.xpath("./td[2]/text()").extract()[0])
            # else:
            #     item['positionType']=u""
            # item['peopleNumber']=str(node.xpath("./td[3]/text()").extract()[0])
            # item['workLocation']=str(node.xpath("./td[4]/text()").extract()[0])
            # item['publishTime']=str(node.xpath("./td[5]/text()").extract()[0])
            #item['markLevel']=str(node.xpath("//div[@class='ri-rating']//div/@class").extract()[0])
            item['markText']=str(node.xpath("string(.)").extract()[0])

            yield item

        if self.offset<300:
            self.offset+=15
            url=self.baseURL+str(self.offset)+self.endword
            yield scrapy.Request(url,callback=self.parse)

        # if len(response.xpath("//a[@class='noactive' and @id='next']"))==0:
        #     url=response.xpath("//a[@id='next']/@href").extract()[0]
        #     yield scrapy.Request("http://hr.tencent.com/"+url,callback=self.parse)

    # def parse_next(selfself,response):
    #     pass

