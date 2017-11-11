# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AppStoreItem(scrapy.Item):
    # define the fields for your item here like:
    userReviewId = scrapy.Field()
    body = scrapy.Field()
    date = scrapy.Field()
    name = scrapy.Field()
    rating = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    storename = scrapy.Field()


class AndriodItem(scrapy.Item):
    # define the fields for your item here like:
    userReviewId = scrapy.Field()
    body = scrapy.Field()
    date = scrapy.Field()
    name = scrapy.Field()
    rating = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()

