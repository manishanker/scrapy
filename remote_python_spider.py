#!/usr/bin/env python2.7

import scrapy
from bs4 import BeautifulSoup

class JobSpider(scrapy.Spider):
    name = 'remote pyhton spider'
    start_urls=['https://www.remotepython.com/jobs/']
    def parse(self, response):
	for title in response.css('h3'):
		yield {'title' : title.css('a ::text').extract_first()}

	for next_page in response.xpath("//div[@class='text-center']/nav/ul/li/a/text()").extract():
	        yield response.follow(next_page, self.parse)
