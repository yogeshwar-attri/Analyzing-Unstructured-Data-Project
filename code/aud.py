# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class AudSpider(scrapy.Spider):
    name = 'aud'
    location='philadelphia'
    allowed_domains = [location+'.craigslist.org']
    start_urls = ['https://'+location+'.craigslist.org/d/tickets/search/tia/']

    def parse(self, response):
        listings = response.xpath('//p[@class="result-info"]')
        for listing in listings:
            listing_title = listing.xpath('a/@href').get()

            low_rel_url = listing.xpath('a/@href').extract_first()
            low_url = response.urljoin(low_rel_url)
            yield Request(low_url, callback=self.parse_lower, meta={'Title': listing_title})

        next_rel_url = response.xpath('//a[@class="button next"]/@href').extract_first()
        next_url = response.urljoin(next_rel_url)
        yield Request(next_url, callback=self.parse)


    def parse_lower(self, response):
        print ('code here')
        date = response.xpath('//span[@class="otherpostings"]/a/text()').get()[-10:]
        response.meta['date'] = date
        yield response.meta

