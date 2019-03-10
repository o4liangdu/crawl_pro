# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['qunar.com']
    #start_urls = ['http://tencent.com/']
    baseURL = "https://travel.qunar.com/search/place/"
    endword = [
        "%25E5%25B9%25BF%25E5%25B7%259E%25E6%2599%25AF%25E7%2582%25B9/0-----0/",
        "%25E9%25A6%2599%25E6%25B8%25AF%25E6%2599%25AF%25E7%2582%25B9/0-----0/",
        "%25E6%25BE%25B3%25E9%2597%25A8%25E6%2599%25AF%25E7%2582%25B9/0-----0/",
        "%25E4%25B8%259C%25E8%258E%259E%25E6%2599%25AF%25E7%2582%25B9/0-----0/",
        "%25E4%25BD%259B%25E5%25B1%25B1%25E6%2599%25AF%25E7%2582%25B9/0-----0/",
        "%25E6%2583%25A0%25E5%25B7%259E%25E6%2599%25AF%25E7%2582%25B9/0-----0/",
        "%25E6%25B1%259F%25E9%2597%25A8%25E6%2599%25AF%25E7%2582%25B9/0-----0/",
        "%25E6%25B7%25B1%25E5%259C%25B3%25E6%2599%25AF%25E7%2582%25B9/0-----0/",
        "%25E8%2582%2587%25E5%25BA%2586%25E6%2599%25AF%25E7%2582%25B9/0-----0/",
        "%25E4%25B8%25AD%25E5%25B1%25B1%25E6%2599%25AF%25E7%2582%25B9/0-----0/",
        "%25E7%258F%25A0%25E6%25B5%25B7%25E6%2599%25AF%25E7%2582%25B9/0-----0/"]
    # 广州，香港，澳门，东莞，佛山，惠州，江门，深圳，肇庆，中山，珠海
    start_urls = []
    #for ew in endword:
    offset = 1
    start_urls = [baseURL + endword[0] + str(offset)]
    # start_urls.append(baseURL+ew+str(offset))

    def parse(self, response):
        #node_list=response.xpath("//div[@class='remark-item clearfix']//div[@class='ri-remarktxt']")
        #for i in range(11):
        url_list = response.xpath("//a[@class='tit']")
        for endurl in url_list:
            print(endurl)
            try:

                yield scrapy.Request(endurl.xpath("./@href").extract()[0], callback=self.parse2)


            except BaseException:
                continue

        if self.offset < 50:
            self.offset += 1
            url = self.baseURL + self.endword[0] + str(self.offset)
            yield scrapy.Request(url, callback=self.parse)
            #i+=1

    def parse2(self, response):
        #node_list=response.xpath("//div[@class='remark-item clearfix']//div[@class='ri-remarktxt']")
        item = TencentItem()
        # item['city']=str(response.xpath("//a[@class='txtlink']").extract()[3])
        # item['city'] = str(response.xpath(
        #     "// *[ @ id = 'js_mainleft'] / div[1] / div / ul / li[5] / a/text()").extract()[0])
        item['city'] = str(response.xpath(
             ".//div[@class='box_l']//a[@class='link_strategy']/text()").extract()[0])
        item['siteName'] = str(response.xpath(
            "//h1[@class='tit']/text()").extract()[0])
        item['markLevel'] = str(response.xpath(
            "//span[@class='cur_score']/text()").extract()[0])
        item['markNumber'] = str(response.xpath(
            "//span[@class='num']/text()").extract()[0]).replace(')','').replace('(','')
        yield item
