# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductscrapyItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    retailer_sku_code = scrapy.Field()
    model = scrapy.Field()
    mpn = scrapy.Field()
    sku = scrapy.Field()
    upc = scrapy.Field()
    ean = scrapy.Field()
    currency = scrapy.Field()
    price = scrapy.Field()
    crawl_time = scrapy.Field()
    promo_price = scrapy.Field()
    promo_qty = scrapy.Field()
    promo_data = scrapy.Field()
    promo_expiry = scrapy.Field()
    current_price = scrapy.Field()
    brand = scrapy.Field()
    primary_image_url = scrapy.Field()
    image_urls = scrapy.Field()
    categories = scrapy.Field()
    attributes = scrapy.Field()
    features = scrapy.Field()
    rating = scrapy.Field()
    instock = scrapy.Field()
    
