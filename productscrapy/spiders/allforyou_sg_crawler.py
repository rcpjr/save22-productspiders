# -*- coding: utf-8 -*-
import scrapy

from productscrapy.items import ProductscrapyItem
from productscrapy.loader.allforyou_sg_loader import AllforyouSgLoader

class Allforyousgcrawler(scrapy.Spider):
    name = "allforyou_sg_crawler"
    allowed_domains = ["allforyou.sg"]
    start_urls = (
        'https://www.allforyou.sg/',
    )

    def parse(self, response):
        for parse in response.xpath('//*[@id="pagemaincontent"]/div[1]/div[2]/div/div/div/div/div[2]/a/@href').extract():
            yield scrapy.Request(response.urljoin(parse), callback=self.parse_dir_contents)
            # print response.urljoin(parse) 
            #printing of main page link

    def parse_dir_contents(self, response):
        for contents in response.xpath('//*[@id="pagemaincontent"]/div[1]/div[2]/div/div/h2/a/@href').extract():
            # print response.urljoin(contents)
            yield scrapy.Request(response.urljoin(contents), callback=self.details)

    def details(self, response):
        loader = AllforyouSgLoader(item = ProductscrapyItem(), response = response)
        for details in response.xpath('//div[@class="prod-data"]/@id').extract():
            loader.add_xpath ('title','//div[@id="'+details+'"]/@data-name')
            loader.add_xpath ('description','//div[@id="'+details+'"]/@data-desc')
            loader.add_xpath ('retailer_sku_code','//div[@id="'+details+'"]/@data-newprodid')
            loader.add_xpath ('url','//div[@id="'+details+'"]/@data-imgurl')
            loader.add_xpath ('promo_data','//div[@id="'+details+'"]/@data-offername')
            #loader.add_xpath ('selqty','//div[@id="'+details+'"]/@data-selqty')
            loader.add_xpath ('price','//div[@id="'+details+'"]/@data-price')
            loader.add_xpath ('current_price','//div[@id="'+details+'"]/@data-price')
            #loader.add_xpath ('add2cart','//div[@id="'+details+'"]/@data-add2cart')
            #loader.add_xpath ('add2list','//div[@id="'+details+'"]/@data-add2list')
            loader.add_xpath ('instock','//div[@id="'+details+'"]/@data-outofstack')
            return loader.load_item()

