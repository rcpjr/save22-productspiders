# -*- coding: utf-8 -*-
import scrapy


class Allforyousgcrawler(scrapy.Spider):
    name = "allforyou_sg_crawler"
    allowed_domains = ["allforyou.sg"]
    start_urls = (
        'https://www.allforyou.sg/',
    )

    def parse(self, response):
        for parse in response.xpath('//*[@id="pagemaincontent"]/div[1]/div[2]/div/div/div/div/div[2]/a/@href').extract():
            print response.urljoin(parse)  

        
