# -*- coding: utf-8 -*-
import scrapy

from productscrapy.items import ProductscrapyItem

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
        item = ProductscrapyItem
        for details in response.xpath('//div[@class="prod-data"]/@id').extract():
            item ['name'] = response.xpath('//div[@id="'+details+'"]/@data-name').extract()[0]
            item ['desc'] = response.xpath('//div[@id="'+details+'"]/@data-desc').extract()[0]
            item ['newprodid'] = response.xpath('//div[@id="'+details+'"]/@data-newprodid').extract()[0]
            item ['tah'] = response.xpath('//div[@id="'+details+'"]/@data-tah').extract()[0]
            item ['imgurl'] = response.xpath('//div[@id="'+details+'"]/@data-imgurl').extract()[0]
            item ['selqty'] = response.xpath('//div[@id="'+details+'"]/@data-selqty').extract()[0]
            item ['price'] = response.xpath('//div[@id="'+details+'"]/@data-price').extract()[0]
            item ['oldprice'] = response.xpath('//div[@id="'+details+'"]/@data-oldprice').extract()[0]
            item ['add2cart'] = response.xpath('//div[@id="'+details+'"]/@data-add2cart').extract()[0]
            item ['add2list'] = response.xpath('//div[@id="'+details+'"]/@data-add2list').extract()[0]
            item ['outofstack'] = response.xpath('//div[@id="'+details+'"]/@data-outofstack').extract()
            yield item