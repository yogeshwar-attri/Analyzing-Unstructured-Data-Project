# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://chicago.craigslist.org/search/cta?']

    def parse(self, response):
        deals=response.xpath('//p[@class="result-info"]')
        
        #titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        for deal in deals:
            title=deal.xpath('a/text()').get()
            city=deal.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').get("missing")[2:-1]
            url=deal.xpath('a/@href').get()
            low_rel_url=deal.xpath('a/@href').get()
            low_url=response.urljoin(low_rel_url)
            yield Request(low_url,callback=self.parse_lower,meta={"Title":title,'city':city,"url":url})
            #yield{'Title':title,'city':city}
            
        next_rel_url=response.xpath('//a[@class="button next"]/@href').get()
        next_url=response.urljoin(next_rel_url)
        yield Request(next_url,callback=self.parse)
    def parse_lower(self, response):
        text = "".join(line for line in response.xpath('//*[@id="postingbody"]/text()').getall())
        response.meta['Text'] = text
        yield response.meta