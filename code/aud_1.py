# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class Aud1Spider(scrapy.Spider):
    name = 'aud_1'
    location='philadelphia'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://'+location+'.craigslist.org/d/cars-trucks/search/cta']


    def parse(self, response):
        listings = response.xpath('//p[@class="result-info"]')
        for listing in listings:
            listing_url = listing.xpath('a/@href').get()

            low_rel_url = listing.xpath('a/@href').extract_first()
            low_url = response.urljoin(low_rel_url)
            yield Request(low_url, callback=self.parse_lower, meta={'Title': listing_url})

        next_rel_url = response.xpath('//a[@class="button next"]/@href').extract_first()
        next_url = response.urljoin(next_rel_url)
        yield Request(next_url, callback=self.parse)

    def parse_lower(self, response):
        date = response.xpath('//time[contains(@class, "timeago")]/@datetime').extract_first()[:10]
        response.meta['date'] = date
        yield response.meta
